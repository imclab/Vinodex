import os
import requests
import tempfile
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.shortcuts import render
from django.utils import simplejson as json
from django.core.cache import cache
from wine.models import Wine, Winery
from wine.api import WineResource
from tastypie.serializers import Serializer
import zxing
=======
from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from wine.models import UserProfile
from wine.forms import NewUserRegistrationForm
>>>>>>> bad_frontend

@login_required
def home(request):
    return render(request,"inventory.html")

<<<<<<< HEAD
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

def render_wines(wines, request):
    """
        Returns an HTTPResponse object containing a list of wines. If the user
        has passed in the `limit` parameter in their request, this is limited
        to that amount. This returns this list of wines in the order they
        were provided to this method
    """
    wr = WineResource()
    rendered_wines = [wr.full_dehydrate(wr.build_bundle(obj=wine, request=request)) for wine in wines]
    response = []
    if request.GET.get("limit"):
        limit = int(request.GET["limit"])
        response = Serializer().serialize(rendered_wines[:limit])
    else:
        response = Serializer().serialize(rendered_wines)

    return HttpResponse(response, mimetype="application/json")

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
    return render_wines(wines_with_wineries + wines_without_wineries, request)

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
    """
        Returns a list of wines that could be matched to a given barcode.
        Takes a `url` parameter with a link to the image
        TODO: Should take a `image` parameter with the actaul image
        uploaded in FILES.
    """
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
=======
class NewUserRegistrationView(RegistrationView):
    form_class = NewUserRegistrationForm

    def create_profile(self, request, user, **cleaned_data):
        first_name, last_name, avatar = (cleaned_data["first_name"],
        cleaned_data["last_name"], cleaned_data.get("avatar"))
        profile = UserProfile(user = user, first_name=first_name, last_name = last_name,
                avatar = avatar)
        profile.save()
        return profile

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        new_user.profile = self.create_profile(request, new_user, **form.cleaned_data)
        new_user.save()
        success_url = self.get_success_url(request, new_user)
        
        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)
>>>>>>> bad_frontend
