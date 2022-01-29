from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import PostForm
from .filters import PostFilter
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(active = True, featured = True)[0:3]
    
    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active = True)
    my_filter = PostFilter(request.GET, queryset=posts)
    posts = my_filter.qs
    
    page= request.GET.get('page')
    
    paginator = Paginator(posts,3)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
        
        
    context = {'posts': posts, 'my_filter':my_filter}
    return render(request, 'base/posts.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    
    context = {'post': post}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')


# CRUD VIEWS: 

@login_required(login_url = 'home')
def create_post(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

@login_required(login_url = 'home')
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

@login_required(login_url = 'home')
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        post.delete()
        return redirect('posts')
        
    context = {'item': post}
    return render(request, 'base/delete.html', context)


def send_email(request):
    
    if request.method == 'POST': 
        template = render_to_string('base/email_template.html',{
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
            
        })
        
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['adrian.adam.zaleski@gmail.com']
        )
        
        email.fail_silentl=False
        email.send()
    return render(request, 'base/email_sent.html')
