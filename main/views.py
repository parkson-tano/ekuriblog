from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Admin
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView, ListView, FormView, View
from .models import Post, Category, SubCategory, Comment
from .forms import CommentForm, PostForm, AdminLoginForm, ContactForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here


class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = Post.objects.last()
        post = Post.objects.filter(
            status='published').order_by('view_count')[2:5]
        post2 = Post.objects.filter(
            status='published').order_by('view_count')[4:8]
        last = Post.objects.first()
        context['first'] = first

        context['last'] = last
        context["post"] = post 
        context['post2'] = post2
        return context


class PostView(TemplateView):
    template_name = 'single-post.html'
    # context_object_name = 'post'
    # model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        post = Post.objects.get(slug=slug)
        post.view_count += 1
        post.save()
        context['post'] = post
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class SearchView(TemplateView):
    template_name = 'search-result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        result = Post.objects.filter(Q(title__icontains=kw) | Q(
            content__icontains=kw) | Q(excerpt__icontains=kw))
        context["result"] = result
        return context


class CategoryDetailView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        allcategory = Category.objects.all()
        category = Category.objects.get(slug=url_slug)
        post = Post.objects.filter(Q(category=category) & Q(status = 'published'))
        context['post'] = post
        context['cat'] = category
        return context

class AdminPostCreateView(CreateView):
    template_name = 'admin/create.html'
    model = Post
    fields = ['author', 'category',
              'title', 'image_1', 'excerpt', 'content', 'status']
    success_url = reverse_lazy('main:list_post')

    def get_queryset(self):
        author = self.request.user
        return super().get_queryset()


class AdminPostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('main:list_post')


class AdminPostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'admin/postlist.html'


class AdminPostUpdateView(UpdateView):
    template_name = 'admin/create.html'
    model = Post
    fields = ['author', 'category',
              'title', 'image_1', 'excerpt', 'content', 'status']
