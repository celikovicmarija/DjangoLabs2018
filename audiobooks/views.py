from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Audiobook
from django.views.generic import DetailView, ListView

class LatestReleasesView(ListView):
    template_name = 'audiobooks/index.html'
    context_object_name = 'recent_audiobooks'

    def get_queryset(self):
        return Audiobook.objects.order_by('-released_date')[:10]

class AudiobookDetail(DetailView):
    template_name = 'audiobooks/book_detail.html'
    model = Audiobook

class DetailAfterReview(DetailView):
    template_name = 'audiobooks/detail_after_review.html'
    model = Audiobook


def handle_error(request, audiobook, err_msg):
    return render(request, 'audiobooks/book_detail.html', {
        'audiobook':audiobook,
        'error_msg':err_msg
    })

def review(request, audiobook_id):
    audiobook = get_object_or_404(Audiobook, id=audiobook_id)

    try:
        rating = request.POST['rating']
        comment = request.POST['comment']
    except KeyError as key_err:
        return handle_error(request, audiobook, str(key_err))

    if rating != "":
        audiobook.review_set.create(rating=rating, comment=comment)
        return HttpResponseRedirect( reverse('audiobooks:after_review', args=(audiobook.id,)))
    else:
        return handle_error(request, audiobook, "ERROR: Rating is required!")


# def book_detail_after_review(request, audiobook_id):
#     audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
#     return render(request, 'audiobooks/detail_after_review.html',
#                   {'audiobook':audiobook})

# def index(request):
#     latest_audiobooks = Audiobook.objects.order_by('-released_date')[:10]
#     context = {'recent_audiobooks':latest_audiobooks}
#     return render(request, 'audiobooks/index.html', context)
#
# def book_detail(request, audiobook_id):
#     an_audiobook = get_object_or_404(Audiobook, id=audiobook_id)
#     context ={
#         'audiobook':an_audiobook
#     }
#     return render(request, 'audiobooks/book_detail.html', context)