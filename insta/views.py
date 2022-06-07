from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'insta/home.html'
    contxt_object_name = ' posts'

def about(request):
    
    
    return render(request, 'insta/about.html')