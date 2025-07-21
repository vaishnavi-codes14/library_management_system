from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date="2025-01-01",
            isbn_number="1234567890123",
            description="A test book description."
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Author Name")