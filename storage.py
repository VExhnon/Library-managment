import json
from book import Book
from typing import List, Dict

class Storage:
    def __init__(self, filename: str):
        """
        Инициализация объекта для работы с хранилищем данных.

        :param filename: Имя файла для хранения данных.
        """
        self.filename: str = filename

    def load_books(self) -> List[Book]:
        """
        Загрузка книг из файла.

        :return: Список загруженных книг.
        """
        try:
            with open(self.filename, 'r') as file:
                books_data: List[Dict] = json.load(file)
                return [self._dict_to_book(data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_books(self, books: List[Book]) -> None:
        """
        Сохранение книг в файл.

        :param books: Список книг для сохранения.
        """
        with open(self.filename, 'w') as file:
            books_data: List[Dict] = [self._book_to_dict(book) for book in books]
            json.dump(books_data, file, indent=4)

    def _book_to_dict(self, book: Book) -> Dict:
        """
        Преобразование объекта книги в словарь.

        :param book: Объект книги.
        :return: Словарь с данными книги.
        """
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "status": book.status
        }

    def _dict_to_book(self, data: Dict) -> Book:
        """
        Преобразование словаря в объект книги.

        :param data: Словарь с данными книги.
        :return: Объект книги.
        """
        book = Book(title=data["title"], author=data["author"], year=data["year"])
        book.id = data["id"]
        book.status = data["status"]
        return book
