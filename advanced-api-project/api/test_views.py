from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Book, Author

User = get_user_model()

class BookAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data once for all tests
        cls.user = User.objects.create_user(
            username='testuser',
            email='user@test.com',
            password='testpass123'
        )
        cls.admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='adminpass123'
        )
        cls.author = Author.objects.create(name='Test Author')
        cls.book = Book.objects.create(
            title='Existing Book',
            publication_year=2020,
            author=cls.author
        )

def setUp(self):
    """Fresh client for each test"""
    self.client.login(username='testuser', password='testpass123') 
    # Explicit login
# CRUD Tests
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
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

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Filtering/Search/Ordering Tests
    def test_filter_by_year(self):
        Book.objects.create(title='New Book', publication_year=2023, author=self.author)
        url = f"{reverse('book-list')}?publication_year=2023"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2023)

    def test_search_books(self):
        url = f"{reverse('book-list')}?search=Existing"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Book')

    # Permission Tests
    def test_update_book_owner(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    def tearDown(self):
        """Cleanup after each test"""
        self.client.logout()    