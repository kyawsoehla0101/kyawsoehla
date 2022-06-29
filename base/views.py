from django.shortcuts import render
from .models import Category, Post
from django.shortcuts import get_object_or_404
    
# Create your views here.
def home(request):
    posts = Post.objects.all()[:3]
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories}
    return render(request,'base/home.html',context)

def detailView(request,pk):
    post = Post.objects.get(pk=pk)
    post_tags = post.tags.all()
    categories = Category.objects.all()
    similarposts = Post.objects.filter(tags__in = post_tags).exclude(pk=pk)
    recentposts = Post.objects.all()[:4]
    context = {'post':post,'categories':categories,'similarposts':similarposts,'recentposts':recentposts}
    return render(request, 'base/detail.html',context)

def categoryView(request,slug):
    category = get_object_or_404(Category, slug=slug)
    categoryposts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    context = {'categoryposts':categoryposts,'categories':categories,'slug':slug}
    return render(request,'base/categorypost.html',context)

def tagView(request,slug):
    tagposts = Post.objects.filter(tags__slug=slug)
    categories = Category.objects.all()
    context = {'tagposts':tagposts,'categories':categories,'slug':slug}
    return render(request,'base/tagpost.html',context)

def error_404(request,exception):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'base/partials/errors/404.html',context)
