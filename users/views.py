from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from auto_catalog.models.posts import Post


@login_required
def home(request):
    post_count = Post.objects.filter(author_id=request.user.id).count()
    return render(request, "users/home.html", {'post_count': post_count,
                                               'user': request.user})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"