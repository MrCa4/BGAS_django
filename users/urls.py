from django.urls import path
from . import views
urlpatterns = [

 path('dashboard/', views.home, name="home"),
 path('signup/', views.SignUp.as_view(), name="signup"),
]