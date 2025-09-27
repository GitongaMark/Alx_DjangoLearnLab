from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from datetime import datetime

class BookAPITestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = User.objects.create_user(username='testuser', password='pass123')
    self.author = Author.objects.create(name='J.K. Rowling')
    self.book_data = {
       'title': 'Harry Potter',
       'publication_year': 1997,
       'author': self.author.id
    }
  def test_create_book_authenticated(self):
    self.client.login(username='testuser', password='pass123')
    response = self.client.post('/api/books/', self.book_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 1)
    self.assertEqual(Book.objects.get().title, 'Harry Potter')
    
  def test_create_book_unauthenticated(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_get_books(self):
          Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
          response = self.client.get('/api/books/')
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data), 1)

  def test_future_publication_year_rejected(self):
        self.client.login(username='testuser', password='pass123')
        future_data = self.book_data.copy()
        future_data['publication_year'] = datetime.now().year + 10
        response = self.client.post('/api/books/', future_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)

  def test_update_book_authenticated(self):
        book = Book.objects.create(title="Old Title", publication_year=2000, author=self.author)
        self.client.login(username='testuser', password='pass123')
        response = self.client.put(f'/api/books/{book.id}/', {
            'title': 'New Title',
            'publication_year': 2001,
            'author': self.author.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'New Title')

  def test_delete_book_authenticated(self):
        book = Book.objects.create(title="To Delete", publication_year=2010, author=self.author)
        self.client.login(username='testuser', password='pass123')
        response = self.client.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

  def test_filter_by_author(self):
        Book.objects.create(title="Book 1", publication_year=2000, author=self.author)
        another_author = Author.objects.create(name="Another Author")
        Book.objects.create(title="Book 2", publication_year=2005, author=another_author)
        response = self.client.get(f'/api/books/?author={self.author.id}')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book 1")

  def test_search_books(self):
        Book.objects.create(title="Python Guide", publication_year=2022, author=self.author)
        response = self.client.get('/api/books/?search=Python')
        self.assertEqual(len(response.data), 1)

  def test_ordering(self):
        Book.objects.create(title="A Book", publication_year=2010, author=self.author)
        Book.objects.create(title="B Book", publication_year=2005, author=self.author)
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.data[0]['publication_year'], 2005)