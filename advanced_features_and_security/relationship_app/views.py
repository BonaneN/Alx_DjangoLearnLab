from typing import Any
from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books
    context = {'books': books}  # ✅ Use 'books' as the key (matches template)
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view for displaying details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context

# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# User login view
class CustomLoginView(LoginView):
    template_name = "login.html"

# User logout view
class CustomLogoutView(LogoutView):
    template_name = "logout.html"

# Homepage view
def index(request):
    return render(request, "index.html")

# Role-based views
def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Permission-based views
@permission_required("relationship_app.can_add_book")
def can_add_book_view(request):
    return render(request, 'relationship_app/can_add_book.html')

@permission_required("relationship_app.can_change_book")
def can_change_book_view(request):
    return render(request, 'relationship_app/can_change_book.html')

@permission_required("relationship_app.can_delete_book")
def can_delete_book_view(request):
    return render(request, 'relationship_app/can_delete_book.html')
