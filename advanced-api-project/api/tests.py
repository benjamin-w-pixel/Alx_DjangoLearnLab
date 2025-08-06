from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Book, Author

User = get_user_model()

class BookAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data that will be used for all test methods
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        cls.admin = User.objects.create_superuser(
            username='admin',
            password='adminpass123'
        )
        cls.author = Author.objects.create(name='J.K. Rowling')
        cls.book = Book.objects.create(
            title='Harry Potter',
            publication_year=2001,
            author=cls.author
        )

    def setUp(self):
        # Clear any existing books (in case they interfere)
        Book.objects.exclude(id=self.book.id).delete()

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check results count in response data
        self.assertEqual(len(response.data['results'] if 'results' in response.data else response.data), 1)

    def test_book_create_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_create_unauthenticated(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Changed from 401 to 403