import os
import requests
import tempfile
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import simplejson as json
from django.core.cache import cache
from wine.models import Wine
from wine.api import WineResource

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

def render_wine(wine, request):
    wr = WineResource()
    bundle = wr.build_bundle(obj=wine, request=request)
    json = wr.serialize(None, wr.full_dehydrate(bundle), "application/json")
    return HttpResponse(json, mimetype="application/json")


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
    wine = Wine.identify_from_label(filename)
    if wine:
        return render_wine(wine, request)
    else:
        response = {"message": "Wine could not be identified, sorry"}
        return HttpResponseNotFound(json.dumps(response),
                mimetype="application/json")
