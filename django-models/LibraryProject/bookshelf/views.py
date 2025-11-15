from django.shortcuts import render

#my inclusions
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = "Welcome to the Book shelf 📚"
    return HttpResponse(response)