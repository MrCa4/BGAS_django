from django.contrib import admin

# Register your models here.
from auto_catalog.models.posts import Post

admin.site.register(Post)