# 📚 Library Management System – Coursework Report
# _1. Introduction_
_What is this application?_
This application is a simple console-based Library Management System written in Python. It allows users to view available books and managers to add or remove books from the system.

_How to run the program?_
Make sure Python is installed on your machine, then run the main file:
`python main.py`

_🧑‍💻 How to use the program?_
On launch, the user enters their name and chooses a role:

`1` for `Manager` (with `password`), `2` for regular `User`

Depending on the role, different actions will be shown:

`User`: View books; Exit.

`Manager`: Add a book; View books; Remove a book; Exit

# ⚙️ 2. Body / Analysis
✅ Functional Requirements & Implementation

➤ Object-Oriented Programming

_Encapsulation_: `Book` class keeps attributes private using double underscores (`__title`, `__author`):
```python
class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
```
_Inheritance & Polymorphism_: `Manager` inherits from `User` and overrides the `show_actions()` method:
```python
class Manager(User):
    def show_actions(self):
        print("\nHi, Manager! Choose your action:")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Remove a Book")
        print("4. Exit")
```

_Abstraction_: `LibraryItem` is an abstract base class (`ABC`) using `@abstractmethod`.
```python
class Book(LibraryItem):
```
➤ Factory Method Pattern

The `UserFactory` class uses the Factory Method pattern to create either a `User` or a `Manager` based on input:
```python
class UserFactory:
    @staticmethod
    def create_user(name, role_input, password=None):
        if role_input == '1' and password == "admin123":
            return Manager(name)
        return User(name)
```
➤ Composition implementation

Class `Library` "Owns" a list of `Book` objects. These objects do not exist independently outside of `Library`.
When you remove or save books, it's always done through `Library`:
```python
class Library:
    def __init__(self):
        self.books = []
```
➤ File Handling (State Persistence)

Books are stored in a file (books.csv), which simulates persistent state:
```python
def save_books(self, filename="books.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(book.to_list() for book in self.books)
```
