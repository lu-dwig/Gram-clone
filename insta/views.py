# from email.mime import image
# from re import template

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PostCreateView(LoginRequiredMixin ,CreateView):
    model= Post
    fields = ['image', 'title',  'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model= Post
    fields = ['image', 'title',  'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeteteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model= Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


 
def about(request):
    
    
    return render(request, 'insta/about.html')