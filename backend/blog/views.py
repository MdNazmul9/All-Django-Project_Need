from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name='blog/post_list.html'
    
class PostCreateView(CreateView):
    pass
class PostDetailView(DetailView):
    pass
class PostUpdateView(UpdateView):
    pass
class PostDeleteView(DeleteView):
    pass
