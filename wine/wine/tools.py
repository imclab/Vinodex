import os
import requests
import tempfile
import zxing
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import simplejson as json
from django.core.cache import cache
from wine.api import WineResource
from wine.decorators import timed

def safe_get(url):
    """ Makes a GET request to the given url. If the request does not succeed,
        then an exception is thrown """
    response = requests.get(url)
    response.raise_for_status()
    return response

def get_filename():
    """ Returns a filename that can be used to store a temporary file. This file
        is guaranteed to be available for at least two hours 
        TODO: For now, this gives each file a .jpg extenstion, it should take
        this as a parameter, also this should be moved to tools"""
    if not cache.get("filename_index"):
        cache.set("filename_index", 1, 7200)
        return "temp/1.jpg"
    else:
        file_num = cache.incr("filename_index")
        return "temp/%d.jpg" % file_num

@timed
def download_file(url):
    """ Downloads a file from the given url. Returns the filename of the downloaded
        file"""
    result = safe_get(url) 
    filename = get_filename()
    handle = open(filename, 'w')
    handle.write(result.content)
    return handle.name

@timed
def get_barcode_from_image(url):
    """
        Returns the barcode number (as a String), analyzed from the 
        barcode at the given url. If no barcode could be found,
        None is returned
    """
    reader = zxing.BarCodeReader("/opt/local/zxing-1.6/")
    barcode = reader.decode(url, try_harder=True)
    if barcode and barcode.raw:
        return barcode.raw.split()[0] # Remove trailing EOL
    else:
        return None

def download_image_from_request(request):

    def download_remote_image(url):
        filename = download_file(url)
        return filename

    def download_uploaded_image(image_file):
        filename = get_filename()
        output_file = open(filename, 'w')
        output_file.write(image_file.read())
        return filename

    if request.GET.get("url"):
        url = request.GET.get("url")
        return download_remote_image(url)
    elif request.FILES.get("image"):
        image_file = request.FILES["image"]
        return download_uploaded_image(image_file)

def bad_request(message):
    response = {"message": message}
    return HttpResponseBadRequest(json.dumps(response),
            mimetype="application/json")

def not_found(message):
    response = {"message": message}
    return HttpResponseNotFound(json.dumps(response),
            mimetype="application/json")

def render_result(wines, wineries, request):
    """
        Returns the result from an OCR or label analysis. The wines are ordered
        by likelihood which organized using two methods:
            1. If OCR / Label analysis could figure any wineries, then wines
               that have been identified that could be matched to a detected 
               winery come before wines that could not be matched
            2. In each section, the wines are ordered by popularity, as
               determined by the wine.com API
        If no wines could be determined, this returns a 404 message
    """

    if not wines:
        return not_found("Wine could not be identified, sorry")

    wines_with_wineries = [wine for wine in wines if wine.winery and wine.winery in wineries]
    wines_without_wineries = [wine for wine in wines if wine not in
            wines_with_wineries]
    return WineResource().render_wines(wines_with_wineries + wines_without_wineries, request)
