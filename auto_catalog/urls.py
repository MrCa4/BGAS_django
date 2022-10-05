from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from auto_catalog.views import *
from auto_catalog.views import post_view

urlpatterns = [
    path('', main_view.index_page),
    path('add_post', post_view.add_post),
    path('delete_post', post_view.delete_post),
    path('posts/', main_view.user_posts),

]

