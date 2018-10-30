from django.shortcuts import render
from core.models import Post
import markdown2

def splash(request):
    return render(request, 'splash.html', {})

def apply(request):
    return render(request, 'apply.html', {})

def read(request):
    post_id = request.GET['post']
    post = Post.objects.get(pk=int(post_id))
    post.body = markdown2.markdown(post.body)
    return render(request, 'read.html', {'post': post})