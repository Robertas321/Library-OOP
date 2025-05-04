import unittest
from library import Book, Library
import os

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.test_book = Book("Test Title", "Test Author", "1234567890")
        self.library.add_book(self.test_book)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].to_list(), ["Test Title", "Test Author", "1234567890"])

    def test_remove_book_valid_index(self):
        self.library.remove_book(0)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book_invalid_index(self):
        self.library.remove_book(99)
        self.assertEqual(len(self.library.books), 1)

    def test_save_and_load_books(self):
        test_filename = "test_books.csv"
        self.library.save_books(filename=test_filename)

        new_library = Library()
        new_library.load_books(filename=test_filename)

        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].to_list(), self.test_book.to_list())

        if os.path.exists(test_filename):
            os.remove(test_filename)

if __name__ == '__main__':
    unittest.main()

