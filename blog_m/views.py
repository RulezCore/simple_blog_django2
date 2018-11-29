from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    return render(request, "blog_m/index.html", {'posts': posts})
