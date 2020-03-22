from django.db import models

from django.urls import reverse
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    text = models.TextField()
    #created_date = models.DateTimeField(auto_now=True)
    #published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')