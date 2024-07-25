import unittest
from library import Library

class TestLibrarySystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Создаем временный файл для тестирования и инициализируем объект библиотеки."""
        cls.test_filename = 'test_library.json'
        cls.library = Library(cls.test_filename)

    @classmethod
    def tearDownClass(cls):
        """Удаляем временный файл после тестов."""
        import os
        if os.path.exists(cls.test_filename):
            os.remove(cls.test_filename)

    def setUp(self):
        """Создаем стартовые данные для тестов."""
        books = self.library.get_all_books()
        if books:
            self.library.remove_book(books[0].id)  # Удаляем первую книгу, если она есть

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book('Test Book', 'Test Author', '2024')
        books = self.library.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'Test Book')
        self.assertEqual(books[0].author, 'Test Author')
        self.assertEqual(books[0].year, '2024')
        self.assertEqual(books[0].status, 'available')

    def test_remove_book(self):
        """Тест удаления книги."""
        self.library.add_book('Test Book', 'Test Author', '2024')
        books = self.library.get_all_books()
        book_id = books[0].id
        self.library.remove_book(book_id)
        books = self.library.get_all_books()
        self.assertEqual(len(books), 0)

    def test_search_books_by_title(self):
        """Тест поиска книг по названию."""
        self.library.add_book('Test Book One', 'Test Author', '2024')
        self.library.add_book('Test Book Two', 'Another Author', '2023')
        results = self.library.search_books('Test Book One')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Test Book One')

    def test_search_books_by_author(self):
        """Тест поиска книг по автору."""
        self.library.add_book('Book by Author A', 'Author A', '2024')
        self.library.add_book('Book by Author B', 'Author B', '2023')
        results = self.library.search_books('Author B')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, 'Author B')

    def test_search_books_by_year(self):
        """Тест поиска книг по году издания."""
        self.library.add_book('Book from 2024', 'Author', '2024')
        self.library.add_book('Book from 2023', 'Author', '2023')
        results = self.library.search_books('2024')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, '2024')

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.library.add_book('Test Book', 'Test Author', '2024')
        books = self.library.get_all_books()
        book_id = books[0].id
        self.library.change_status(book_id, 'issued')
        updated_book = self.library.find_book_by_id(book_id)
        self.assertEqual(updated_book.status, 'issued')
        self.library.change_status(book_id, 'available')
        updated_book = self.library.find_book_by_id(book_id)
        self.assertEqual(updated_book.status, 'available')

    def test_invalid_status(self):
        """Тест обработки некорректного статуса при изменении статуса книги."""
        self.library.add_book('Test Book', 'Test Author', '2024')
        books = self.library.get_all_books()
        book_id = books[0].id

        # Заменяем стандартный ввод для проверки обработки ошибки
        from io import StringIO
        import sys
        original_stdin = sys.stdin

        try:
            sys.stdin = StringIO('invalid_status\navailable\n')
            with self.assertRaises(SystemExit):  # Ожидаем завершения программы из-за некорректного статуса
                self.library.change_status(book_id, 'invalid_status')
            updated_book = self.library.find_book_by_id(book_id)
            self.assertEqual(updated_book.status, 'available')
        finally:
            sys.stdin = original_stdin

    def test_load_books(self):
        """Тест загрузки книг из файла."""
        self.library.add_book('Loaded Book', 'Author', '2024')
        self.library = None  # Удаляем ссылку на старую библиотеку
        self.library = Library(self.test_filename)  # Загружаем библиотеку снова
        books = self.library.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'Loaded Book')

    def test_save_books(self):
        """Тест сохранения книг в файл."""
        self.library.add_book('Saved Book', 'Author', '2024')
        self.library = None  # Удаляем ссылку на старую библиотеку
        self.library = Library(self.test_filename)  # Загружаем библиотеку снова
        books = self.library.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'Saved Book')


if __name__ == '__main__':
    unittest.main()
