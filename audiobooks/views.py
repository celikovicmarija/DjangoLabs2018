from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! This is the landing page for our audiobooks app")
