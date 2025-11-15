from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import Book, Author, Library


# Basic views
def index(request):
    return render(request, "relationship_app/index.html")


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Library detail (CBV)
from django.views.generic import DetailView


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ----------------------------
# Authentication
# ----------------------------

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("relationship_app:list_books")
    else:
        form = CustomUserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("relationship_app:list_books")
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("relationship_app:login")


# ----------------------------
# ROLE-BASED ACCESS CONTROL
# ----------------------------

def is_admin(user):
    return user.groups.filter(name="Admin").exists()


def is_librarian(user):
    return user.groups.filter(name="Librarian").exists()


def is_member(user):
    return user.groups.filter(name="Member").exists()


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# ----------------------------
# Permission-based CRUD
# ----------------------------

@permission_required("relationship_app.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        Book.objects.create(title=title, author_id=author_id)
        return redirect("relationship_app:list_books")

    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})


@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.publication_year = request.POST.get("year")
        book.save()
        return redirect("relationship_app:list_books")

    return render(request, "relationship_app/edit_book.html", {"book": book})


@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("relationship_app:list_books")

    return render(request, "relationship_app/delete_book.html", {"book": book})
