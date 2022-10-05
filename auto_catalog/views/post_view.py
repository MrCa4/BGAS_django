import datetime
import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from auto_catalog.forms.post_form import PostForm
from auto_catalog.models.posts import Post
from djangoBGAS.settings import MEDIA_URL, IMG_URL, MEDIA_ROOT, BASE_DIR


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['img']
            fs = FileSystemStorage(location=os.path.join(MEDIA_ROOT, 'img'))
            filename = fs.save(file.name, file)
            file_url = fs.url(os.path.join(IMG_URL, filename))
            post = Post(title=request.POST.get('post_title'),
                        img=file_url,
                        author_id=request.user.id
                        )
            post.save()



            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

@login_required
def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.filter(id=post_id).first()
        if post.author_id == request.user.id:
            Post.delete(post)
    return HttpResponseRedirect('/accounts/posts')