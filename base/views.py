from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def posts(request):
    
    posts= [
        {
            'headline': 'To Do app',
            'sub_headline': ' First app made. Simple to do app.',
        },
        
        {
            'headline': 'Coś tam coś tam',
            'sub_headline': 'Some text here. Need more text.Some text here. Need more text.Some text here. Need more text.Some text here. Need more text.Some text here. Need more text.',
        },
        
        {
            'headline': 'Need of Title',
            'sub_headline': 'KOlejna partia tekstu tutaj',
        },
    ]
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')