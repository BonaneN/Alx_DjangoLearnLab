from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm, BookForm


#my inclusions
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = "Welcome to the Book shelf 📚"
    return HttpResponse(response)

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def form_example(request):
    form = ExampleForm()
    return render(request, "form_example.html", {"form": form})


@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "form_example.html", {"form": form})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("book_list")
