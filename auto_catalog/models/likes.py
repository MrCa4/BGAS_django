from django.contrib.auth.models import User
from django.db import models

from auto_catalog.models.posts import Post


class Likes(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    folows = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    folowers = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Likes"
