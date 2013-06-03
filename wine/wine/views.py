import os
import requests
import tempfile
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from wine.models import Wine, Winery, UserProfile, User, Bottle
from wine.api import WineResource
from django.views.decorators.csrf import csrf_exempt
from tastypie.serializers import Serializer
import zxing
from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from wine.forms import NewUserRegistrationForm
from django.utils import simplejson as json
from tools import (safe_get, download_file, get_filename,
                   get_barcode_from_image, render_result,
                   download_image_from_request, bad_request, not_found,
                   success, download_bottle_image_from_request)

from forgot_password import send_password_forgot_message, decrypt_userid

def home(request):
    return render(request,"landing.html")

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
            return None, bad_request("A barcode or image is required")

    barcode, response = get_barcode(request)
    if not barcode:
        return response

    wines = Wine().identify_from_barcode(barcode)
    wineries = Winery().identify_from_barcode(barcode)
    return render_result(wines, wineries, request)

@csrf_exempt
def wine_label_upload(request):
    filename = download_bottle_image_from_request(request)
    bottle = Bottle.objects.get(id=request.GET["bottle_id"])
    bottle.wine.label_photo =  "http://vinodex.us/images/" + filename
    print bottle.wine.label_photo
    bottle.wine.save()
    return success({filename: filename})
    
     
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
            return None, bad_request("An image file is required")

    filename, response = get_image_filename(request)
    if not filename:
        return response

    wines = Wine().identify_from_label(filename)
    wineries = Winery().identify_from_label(filename)
    return render_result(wines, wineries, request)

@csrf_exempt
def forgot_password(request):
    email = request.POST.get("email")
    if not email:
        return not_found("An e-mail is required")

    users = User.objects.filter(email=email)
    if not users:
        return not_found("User with email %s does not exist." % email)
    else:
        send_password_forgot_message(users[0])
        return HttpResponse(json.dumps({"message": "success"}))

@csrf_exempt
def reset_password(request):
    cipher = request.POST.get("cipher")
    password = request.POST.get("password")
    if not password or not cipher:
        return bad_request("A cipher and password are required to reset password")
    user_id = decrypt_userid(cipher)
    user = User.objects.filter(id=user_id)
    user.update(password=password)
    return HttpResponse(json.dumps({"message": "success"}))

@csrf_exempt
def sommelier(request):
    wine_types = request.GET.get("wine_types[]")
    if not wine_types:
        return not_found("No wine types were provided")
    
    wines = Wine.objects.filter(wine_type__in=wine_types).order_by('?')[:10]
    return WineResource().render_wines(wines, request)
