from django.http.response import HttpResponse 
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(active = True, featured = True)[0:3]
    
    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active = True)
    
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    
    context = {'post': post}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')


# CRUD VIEWS: 

def create_post(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

