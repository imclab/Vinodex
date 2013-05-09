import os
import requests
import tempfile
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import simplejson as json
from django.core.cache import cache
from wine.api import WineResource

SCANDIT_URL = "https://api.scandit.com/v2/products/"
API_KEY = "QMXnoEqepvSpQe0cRC--7PUBKocQQmMoN29FxKYMO96"

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

def download_file(url):
    """ Downloads a file from the given url. Returns the filename of the downloaded
        file"""
    result = safe_get(url) 
    filename = get_filename()
    handle = open(filename, 'w')
    handle.write(result.content)
    return handle.name

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
        response = {"message": "Wine could not be identified, sorry"}
        return HttpResponseNotFound(json.dumps(response),
                mimetype="application/json")

    wines_with_wineries = [wine for wine in wines if wine.winery and wine.winery in wineries]
    wines_without_wineries = [wine for wine in wines if wine not in
            wines_with_wineries]
    return WineResource().render_wines(wines_with_wineries + wines_without_wineries, request)
