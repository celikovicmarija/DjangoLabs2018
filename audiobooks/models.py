from django.db import models
from datetime import date, datetime

class Audiobook(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    narrator = models.CharField(max_length=200, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    released_date = models.DateField(null=True, blank=True)

    def __str__(self):
        audiobook_str = "title: " + self.title
        audiobook_str += "\nauthor: {}".format(self.author) if self.author else ""
        audiobook_str += "\nnarrator: {}".format(self.narrator) if self.narrator else ""
        audiobook_str += "\nlength: {}".format(self.format_length()) if self.length else ""
        audiobook_str += "\nreleased date: {}".format(self.format_date()) if self.released_date else ""
        return audiobook_str

    def format_length(self):
        if self.length:
            hour, min = divmod(self.length, 60)
            return "{}hrs {}mins".format(hour, min)
        else:
            return "unknown"

    def format_date(self):
        if self.released_date:
            return date.strftime(self.released_date, "%d-%m-%y")
        else:
            return "unknown"

class Review(models.Model):

    rating = models.IntegerField()
    comment = models.CharField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    for_audiobook = models.ForeignKey(to=Audiobook, on_delete=models.CASCADE)

    def __str__(self):
        review_str = "rating: {} stars".format(self.rating)
        review_str += "\ncomment: {}".format(self.comment) if self.comment else ""
        review_str += "\ndatetime posted: " + datetime.strftime(self.timestamp, "%d-%m-%y %H:%M")
        return review_str