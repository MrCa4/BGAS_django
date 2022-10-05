import datetime

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    # id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="img")
    date = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.title


