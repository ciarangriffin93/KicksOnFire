from django.shortcuts import render
from .models import BlogPost

def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_post_list.html', {'posts': posts})