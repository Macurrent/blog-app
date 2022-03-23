from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Post


class BlogListView(ListView):
    '''This class lists all that is in our database'''
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):  # new
    '''Viewing a post posted by individual person. The first post will be given an id of 1, the second 2...'''
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    '''Creating a form where users will be able to write something which will again be stored in the database'''
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):  # new
    '''Creating update/edit form'''
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
