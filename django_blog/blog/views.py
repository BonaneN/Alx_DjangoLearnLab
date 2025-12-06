from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from typing import cast
from .models import Post, Comment, Tag
from .forms import RegistrationForm, CommentForm

# Authentication Views

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


# Post Views (CRUD)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
    # Assign the author
        form.instance.author = self.request.user

    # Save the post object
        post = form.save()

    # Handle tags (if using a custom Tag model)
        tags_str = form.cleaned_data.get("tags")  # Corrected syntax
    
        if tags_str:
            tags = [name.strip() for name in tags_str.split(",")]
            for name in tags:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                post.tags.add(tag_obj)
    
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = cast(Post, self.get_object())
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = cast(Post, self.get_object())
        return post.author == self.request.user


# Comment Views (CRUD)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_pk)
        form.instance.post = post
        form.instance.author = self.request.user
        form.save()
        return redirect('post_detail', pk=post.pk)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = cast(Comment, self.get_object())
        return comment.author == self.request.user

    def form_valid(self, form):
        comment = cast(Comment, form.save())
        return redirect('post_detail', pk=comment.post.pk)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def test_func(self):
        comment = cast(Comment, self.get_object())
        return comment.author == self.request.user

    def post(self, request, *args, **kwargs):
        comment = cast(Comment, self.get_object())
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
