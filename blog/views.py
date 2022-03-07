from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User, Post


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostView(DetailView):
    model = Post
    template_name = 'post.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add.html'

    fields = '__all__'