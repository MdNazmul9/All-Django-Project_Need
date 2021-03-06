from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Post
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from blog.models import Post
    
class HomeView(TemplateView):
    model = Post
    context_object_name = 'post_list'
    template_name='home.html'
    
class DashboardView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'post_list'
    template_name='dashboard.html'

