import uuid

class Book:
    def __init__(self, title: str, author: str, year: str):
        """
        Инициализация объекта книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        self.id: str = str(uuid.uuid4())  # Генерация уникального идентификатора
        self.title: str = title
        self.author: str = author
        self.year: str = year
        self.status: str = "available"

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строковое представление книги.
        """
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"
