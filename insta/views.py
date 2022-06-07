from email.mime import image
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model= Post


class PostCreateView(CreateView):
    model= Post
    fields = ['image', 'title',  'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def about(request):
    
    
    return render(request, 'insta/about.html')