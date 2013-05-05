from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return HttpResponse("You are now logged in.")
