from django.urls import path, include
from .views import DashboardView,HomeView 
urlpatterns = [
    path('',HomeView.as_view(),name ='home'),
    path('dashboard/',DashboardView.as_view(),name ='dashboard')
]