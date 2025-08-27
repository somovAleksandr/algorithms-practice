def add_book(books, title, author, year):
    if not title.strip():
        return "Ошибка: название не может быть пустым."
    if not author.strip():
        return "Ошибка: автор не может быть пустым."
    if not isinstance(year, int) or year <= 0:
        return "Ошибка: год должен быть положительным числом."

    for book in books:
        if book["title"].lower() == title.lower():
            return f"Ошибка: книга '{title}' уже есть в библиотеке."

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "available": True
    })
    return f"Книга '{title}' добавлена."


def show_all_books(books):
    if not books:
        print("Библиотека пуста.")
        return

    print("\n--- Все книги ---")
    for book in books:
        status = "Доступна" if book["available"] else f"Выдана: {book.get('borrowed_by', 'Неизвестно')}"
        print(f"• '{book['title']}' — {book['author']} ({book['year']}) [{status}]")
    print("-" * 20)


def find_book(books, query):
    if not query.strip():
        return []

    query = query.lower().strip()
    results = []
    for book in books:
        if (query in book["title"].lower() or
            query in book["author"].lower()):
            results.append(book)
    return results


def remove_book(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            return f"Книга '{title}' удалена."
    return f"Книга '{title}' не найдена."


def borrow_book(books, title, reader):
    if not reader.strip():
        return "Ошибка: имя читателя не может быть пустым."

    for book in books:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                return f"Книга '{title}' уже выдана."
            book["available"] = False
            book["borrowed_by"] = reader
            return f"Книга '{title}' успешно выдана {reader}."
    return f"Книга '{title}' не найдена в библиотеке."


def return_book(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            if book["available"]:
                return f"Книга '{title}' и так в библиотеке."
            del book["borrowed_by"]
            book["available"] = True
            return f"Книга '{title}' успешно возвращена."
    return f"Книга '{title}' не найдена в библиотеке."


def main():
    books = []
    print("📚 Добро пожаловать в систему управления библиотекой!")

    while True:
        print("\n=== Меню ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу")
        print("4. Удалить книгу")
        print("5. Выдать книгу")
        print("6. Вернуть книгу")
        print("7. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Название: ").strip()
            author = input("Автор: ").strip()
            try:
                year = int(input("Год: "))
            except ValueError:
                print("Год должен быть числом!")
                continue
            print(add_book(books, title, author, year))

        elif choice == "2":
            show_all_books(books)

        elif choice == "3":
            query = input("Поиск (по названию или автору): ").strip()
            results = find_book(books, query)
            if results:
                print(f"\nНайдено {len(results)} книг(и):")
                for book in results:
                    status = "Доступна" if book["available"] else f"Выдана: {book.get('borrowed_by')}"
                    print(f"• '{book['title']}' — {book['author']} ({book['year']}) [{status}]")
            else:
                print("Ничего не найдено.")

        elif choice == "4":
            title = input("Название книги для удаления: ").strip()
            print(remove_book(books, title))

        elif choice == "5":
            title = input("Название книги: ").strip()
            reader = input("Имя читателя: ").strip()
            print(borrow_book(books, title, reader))

        elif choice == "6":
            title = input("Название возвращаемой книги: ").strip()
            print(return_book(books, title))

        elif choice == "7":
            print("До свидания! Хорошего дня! 📖")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()