from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('profile/<username>/', views.profile, name='profile'),
    # path('single_post', views.single_post, name='single_post'),
    
]