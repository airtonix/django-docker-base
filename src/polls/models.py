import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime


class Question(models.Model):

    question_text = models.CharField(max_length=200, default=" ")
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    choice_text = models.CharField(max_length=200, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text