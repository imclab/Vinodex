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
from django.views.decorators.csrf import csrf_exempt
from tastypie.serializers import Serializer
from tools import (safe_get, download_file, get_filename,
                   get_barcode_from_image, render_result,
                   download_image_from_request)

@login_required
def home(request):
    return render(request,"inventory.html")

def upload_image(request):
    return render(request,"upload.html")

@csrf_exempt
def wine_barcode(request):
    """
        Returns a list of wines that could be matched to a given barcode.
        Can take either a `barcode` parameter with the actual code,
        a `url` parameter with the url containing the barcode image.
        TODO: Should take a `image` parameter with the actaul image
        uploaded in FILES.
    """
    def get_barcode(request):
        if request.GET.get("barcode"):
            return request.GET["barcode"], None
        
        image_filename = download_image_from_request(request)
        if image_filename:
            return get_barcode_from_image(image_filename), None
        else:
            return None, badRequest("A barcode or image is required")

    barcode, response = get_barcode(request)
    if not barcode:
        return response

    wines = Wine().identify_from_barcode(barcode)
    wineries = Winery().identify_from_barcode(barcode)
    return render_result(wines, wineries, request)
    
     
@csrf_exempt
def wine_ocr(request):
    """
        Returns a list of wines that could be matched to a given barcode.
        Takes a `url` parameter with a link to the image
        TODO: Should take a `image` parameter with the actaul image
        uploaded in FILES.
    """
    def get_image_filename(request):
        image_filename = download_image_from_request(request)
        if image_filename:
            return image_filename, None
        elif not request.GET.get("url"):
            return None, badRequest("An image file is required")

    filename, response = get_image_filename(request)
    if not filename:
        return response

    wines = Wine().identify_from_label(filename)
    wineries = Winery().identify_from_label(filename)
    return render_result(wines, wineries, request)
