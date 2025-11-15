from django import forms
from .models import Book


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title"]
