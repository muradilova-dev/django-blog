from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Post
from .forms import PostForm, CategoryForm

# Views для категорий
class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/category_form.html'
    success_url = '/categories/'

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/category_form.html'
    success_url = '/categories/'

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'blog/category_confirm_delete.html'
    success_url = '/categories/'

# Views для постов
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/posts/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'