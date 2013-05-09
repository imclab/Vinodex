import os
import requests
import tempfile
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import simplejson as json
from django.core.cache import cache
from wine.models import Wine, Winery
from wine.api import WineResource
from tastypie.serializers import Serializer
import zxing

@login_required
def home(request):
    return render(request,"inventory.html")

def safe_get(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def get_filename():
    if not cache.get("filename_index"):
        cache.set("filename_index", 1, 7200)
        return "temp/1.jpg"
    else:
        file_num = cache.incr("filename_index")
        return "temp/%d.jpg" % file_num

def download_file(url):
    result = safe_get(url) 
    filename = get_filename()
    handle = open(filename, 'w')
    handle.write(result.content)
    return handle.name

def render_wines(wines, request):
    wr = WineResource()
    rendered_wines = [wr.full_dehydrate(wr.build_bundle(obj=wine, request=request)) for wine in wines]
    response = []
    if request.GET.get("limit"):
        limit = int(request.GET["limit"])
        response = Serializer().serialize(rendered_wines[:limit])
    else:
        response = Serializer().serialize(rendered_wines)

    return HttpResponse(response, mimetype="application/json")

def find_best_match(wines, wineries):
    for wine in wines:
        if wine.winery in wineries:
            return wine

    # No match found
    return wines[0]

def get_barcode_from_image(url):
    reader = zxing.BarCodeReader("/opt/local/zxing-1.6/")
    barcode = reader.decode(url, try_harder=True)
    if barcode and barcode.raw:
        return barcode.raw.split()[0] # Remove trailing EOL
    else:
        return None

def render_result(wines, wineries, request):
    if not wines:
        response = {"message": "Wine could not be identified, sorry"}
        return HttpResponseNotFound(json.dumps(response),
                mimetype="application/json")

    wines_with_wineries = [wine for wine in wines if wine.winery and wine.winery in wineries]
    wines_without_wineries = [wine for wine in wines if wine not in
            wines_with_wineries]
    return render_wines(wines_with_wineries + wines_without_wineries, request)

def wine_barcode(request):
    def get_barcode(request):
        if request.GET.get("barcode"):
            return request.GET["barcode"], None
        elif request.GET.get("url"):
            return get_barcode_from_image(request.GET["url"]), None
        else:
            response = {"message": "Either `url` or `barcode` is required"}
            return None, HttpResponseBadRequest(json.dumps(response),
                    mimetype="application/json")

    barcode, response = get_barcode(request)
    if not barcode:
        return response

    wines = Wine().identify_from_barcode(barcode)
    wineries = Winery().identify_from_barcode(barcode)
    return render_result(wines, wineries, request)
    
     
def wine_ocr(request):
    def get_url(request):
        if not request.GET.get("url"):
            response = {"message": "The parameter `url` is required"}
            return None, HttpResponseBadRequest(json.dumps(response),
                    mimetype="application/json")
        return request.GET["url"], None

    url, response = get_url(request)
    if not url:
        return response
    filename = download_file(url)
    wines = Wine().identify_from_label(filename)
    wineries = Winery().identify_from_label(filename)
    return render_result(wines, wineries, request)
