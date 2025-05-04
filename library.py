import csv
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def display_info(self):
        print(f"{self.__title} by {self.__author} (ISBN: {self.__isbn})")

    def to_list(self):
        return [self.__title, self.__author, self.__isbn]

class User:
    def __init__(self, name):
        self.name = name
        self.role = "user"

    def show_actions(self):
        print("\nHi, User! Choose your action:")
        print("1. View Books")
        print("2. Exit")

class Manager(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "manager"

    def show_actions(self):
        print("\nHi, Manager! Choose your action:")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Remove a Book")
        print("4. Exit")

class Library:
                
    def __init__(self):
        self.books = []

    def remove_book(self, index):
        if 0 <= index < len(self.books):
            removed_book = self.books.pop(index)
            print(f"Removed book:")
            removed_book.display_info()
            print("")
            self.save_books()
        else:
            print("❌ Invalid index. No book removed.")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def display_books(self):
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. ", end="")
            book.display_info()

    def save_books(self, filename="books.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(book.to_list() for book in self.books)

    def load_books(self, filename="books.csv"):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                self.books = [Book(*row) for row in reader if row]
        except FileNotFoundError:
            print("No books in library!")
            pass

class UserFactory:
    @staticmethod
    def create_user(name, role_input, password=None):
        if role_input == '1':
            if password == "admin123":
                return Manager(name)
            else:
                print("❌ Wrong password. Logged in as User instead.")
        return User(name)


