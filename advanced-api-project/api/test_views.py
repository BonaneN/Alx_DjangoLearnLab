from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(title='Harry Potter', publication_year=1997, author=self.author)
        self.client = APIClient()

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Harry Potter')

    def test_book_create_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_update_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-update', args=[self.book.pk])
        data = {'title': 'Updated Book', 'publication_year': 2000, 'author': self.author.pk}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-delete', args=[self.book.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
