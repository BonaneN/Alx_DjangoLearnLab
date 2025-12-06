from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from typing import cast


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'  # Specify your custom login template

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'  # Specify your custom logout template

@login_required
def profile(request):
    return render(request, 'blog/profile.html')  # Render a profile page for logged-in users

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Specify your template name
    context_object_name = 'posts'
    ordering = ["-published_date"]

class PostDetailView (DetailView):
    model = Post
    template_name = "blog/post_details.html"

# 
class PostCreateView (LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid (self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    def test_func(self):
        post = cast(Post, self.get_object())
        return post.author == self.request.user
    
class PostDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    template_name = "blog/post_delete.html"

    def test_func(self):
        post = cast(Post, self.get_object())
        return post.author == self.request.user