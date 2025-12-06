from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm

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