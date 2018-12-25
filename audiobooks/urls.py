from django.urls import path
from . import views

app_name = 'audiobooks'

urlpatterns = [
    # audiobooks/
    # path("", views.index, name='index'),
    path("", views.LatestReleasesView.as_view(), name = 'index'),

    # audiobooks/5/
    # path("<int:audiobook_id>/", views.book_detail, name='detail'),
    path("<int:pk>/", views.AudiobookDetail.as_view(), name='detail'),

    # audiobooks/5/review/
    path("<int:audiobook_id>/review/", views.review, name = 'review'),

    # audiobooks/5/after_review
    # path("<int:audiobook_id>/after_review/", views.book_detail_after_review, name = 'after_review'),
    path("<int:pk>/after_review/", views.DetailAfterReview.as_view(), name = 'after_review'),
]