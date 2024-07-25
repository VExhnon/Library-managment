import sys
from library import Library

def add_book(library: Library) -> None:
    """
    Запрашивает у пользователя данные для добавления новой книги и добавляет её в библиотеку.

    :param library: Объект библиотеки.
    """
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    library.add_book(title, author, year)

def remove_book(library: Library) -> None:
    """
    Запрашивает у пользователя идентификатор книги для её удаления из библиотеки.

    :param library: Объект библиотеки.
    """
    book_id = input("Enter book id to remove: ")
    library.remove_book(book_id)

def search_books(library: Library) -> None:
    """
    Запрашивает у пользователя ключевое слово для поиска книг и отображает найденные книги.

    :param library: Объект библиотеки.
    """
    keyword = input("Enter title, author, or year to search: ")
    results = library.search_books(keyword)
    for book in results:
        print(book)

def display_books(library: Library) -> None:
    """
    Отображает список всех книг в библиотеке.

    :param library: Объект библиотеки.
    """
    books = library.get_all_books()
    for book in books:
        print(book)

def change_status(library: Library) -> None:
    """
    Запрашивает у пользователя идентификатор книги и новый статус для изменения статуса книги.

    :param library: Объект библиотеки.
    """
    book_id = input("Enter book id to change status: ")
    status = input("Enter new status ('available' or 'issued'): ")
    library.change_status(book_id, status)

def exit_program(library: Library) -> None:
    """
    Завершает работу программы.

    :param library: Объект библиотеки.
    """
    sys.exit()

def invalid_choice(library: Library) -> None:
    """
    Сообщает пользователю о недопустимом выборе.

    :param library: Объект библиотеки.
    """
    print("Invalid choice. Please try again.")

def main() -> None:
    """
    Основная функция, запускающая приложение и отображающая меню для взаимодействия с пользователем.
    """
    library = Library('library.json')
    actions = {
        '1': add_book,
        '2': remove_book,
        '3': search_books,
        '4': display_books,
        '5': change_status,
        '6': exit_program
    }

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Change book status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        action = actions.get(choice, invalid_choice)
        action(library)

if __name__ == "__main__":
    main()
