from book import Book
from storage import Storage
from typing import List, Optional

class Library:
    def __init__(self, filename: str):
        """
        Инициализация объекта библиотеки.

        :param filename: Имя файла для хранения данных.
        """
        self.storage: Storage = Storage(filename)
        self.books: List[Book] = self.storage.load_books()

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавление книги в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        book: Book = Book(title=title, author=author, year=year)
        self.books.append(book)
        self.storage.save_books(self.books)
        print(f"Book '{title}' added with ID {book.id}")

    def remove_book(self, book_id: str) -> None:
        """
        Удаление книги из библиотеки по идентификатору.

        :param book_id: Идентификатор книги.
        """
        book: Optional[Book] = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.storage.save_books(self.books)
            print(f"Book with ID {book_id} removed.")
        else:
            print(f"No book found with ID {book_id}.")

    def search_books(self, keyword: str) -> List[Book]:
        """
        Поиск книг по ключевому слову.

        :param keyword: Ключевое слово для поиска.
        :return: Список найденных книг.
        """
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword == book.year]

    def get_all_books(self) -> List[Book]:
        """
        Получение списка всех книг.

        :return: Список всех книг.
        """
        return self.books

    def change_status(self, book_id: str, status: str) -> None:
        """
        Изменение статуса книги по идентификатору.

        :param book_id: Идентификатор книги.
        :param status: Новый статус книги.
        """
        book: Optional[Book] = self.find_book_by_id(book_id)
        if book:
            valid_statuses = ["available", "issued"]
            while status not in valid_statuses:
                print("Invalid status. Please enter 'available' or 'issued'.")
                status = input("Enter new status ('available' or 'issued'): ")
            book.status = status
            self.storage.save_books(self.books)
            print(f"Status of book ID {book_id} changed to {status}.")
        else:
            print(f"No book found with ID {book_id}.")

    def find_book_by_id(self, book_id: str) -> Optional[Book]:
        """
        Поиск книги по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Найденная книга или None, если книга не найдена.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None
