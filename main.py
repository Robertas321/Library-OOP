from abc import ABC, abstractmethod
import csv
from library import LibraryItem,  User, Book, Manager, Library, UserFactory


def main():
    name = input("Enter your name: ")
    role_input = input("Login as (1 - Manager, 2 - User): ")


    if role_input == '1':
        password = input("Enter manager password: ")
        user = UserFactory.create_user(name, role_input, password)
    else:
        user = UserFactory.create_user(name, role_input)


    library = Library()
    library.load_books()

    while True:
        user.show_actions()
        choice = input("Choose an option: ")

        if choice == '1':
            if user.role == "manager":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                library.add_book(Book(title, author, isbn))
            else:
                library.display_books()

        elif choice == '2':
            if user.role == "manager":
                library.display_books()
            else:
                print("👋 Goodbye!")
                break

        elif choice == '3' and user.role == "manager":
            library.display_books()
            try:
                 book_number = int(input("Enter the number of the book to remove: ")) - 1
                 library.remove_book(book_number)
            except ValueError:
                print("❌ Please enter a valid number.")
            else:
                print("✅ Book removed successfully.")

        elif choice == '4' and user.role == "manager":
            print("👋 Goodbye!")
            break

        else:
                print("❌ Invalid choice.")




if __name__ == "__main__":
    main()
