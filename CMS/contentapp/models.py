from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100000)
    when_created = models.DateTimeField(default=datetime.now, blank=True)
