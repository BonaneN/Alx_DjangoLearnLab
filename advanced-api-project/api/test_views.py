from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', email='email',password='adminpass')

        # Create author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=2002, author=self.author)

    # -----------------------------
    # LIST BOOKS
    # -----------------------------
    def test_list_books_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -----------------------------
    # GET SINGLE BOOK
    # -----------------------------
    def test_get_single_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # -----------------------------
    # CREATE BOOK (admin only)
    # -----------------------------
    def test_create_book_admin_only(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.pk
        }

        # Normal user → forbidden
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Admin → allowed
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    # -----------------------------
    # UPDATE BOOK
    # -----------------------------
    def test_update_book_admin_only(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('book-update', args=[self.book1.pk])
        data = {"title": "Updated Title", "publication_year": 2000, "author": self.author.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # -----------------------------
    # DELETE BOOK
    # -----------------------------
    def test_delete_book_admin_only(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('book-delete', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # FILTER BOOKS
    # -----------------------------
    def test_filter_books_by_title(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list') + f'?title=Harry Potter 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter 1")

    # -----------------------------
    # SEARCH BOOKS
    # -----------------------------
    def test_search_books_by_title(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list') + '?search=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -----------------------------
    # ORDER BOOKS
    # -----------------------------
    def test_order_books_by_year_desc(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter 2")
