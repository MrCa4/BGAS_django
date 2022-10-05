from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from auto_catalog.models.posts import Post


def index_page(request):
    post_list = Post.objects.order_by('-id')
    return view(post_list, request)



@login_required
def user_posts(request):
    post_list = Post.objects.order_by('-id').filter(author_id=request.user.id)
    return view(post_list, request, del_perm=True)


def view(post_list, request, del_perm=False):
    paginator = Paginator(post_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj,'del_perm':del_perm})