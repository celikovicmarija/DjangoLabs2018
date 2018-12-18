from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Audiobook

def index(request):
    return HttpResponse("Hello! This is the landing page for our audiobooks app")

def book_detail(request, audiobook_id):
    an_audiobook = get_object_or_404(Audiobook, id=audiobook_id)
    context ={
        'audiobook':an_audiobook
    }
    return render(request, 'audiobooks/book_detail.html', context)

def review(request, audiobook_id):
    return HttpResponse("This view will process new review "
                        "for audiobook with id {}".format(audiobook_id))

def book_detail_after_review(request, audiobook_id):
    return HttpResponse("This page will present detailed info with the latest review "
                        "for audiobook with id {}".format(audiobook_id))