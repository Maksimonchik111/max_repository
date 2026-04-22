import sqlite3

def create_table(conn):
    conn.execute("""
        DROP TABLE IF EXISTS books
        """)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER 
        )
        """
    )


def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
        """
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()


def get_all_books(conn):
    result = conn.execute("""
    SELECT * FROM books
    """)
    return result.fetchall()

def get_books_by_author(conn, author):
    result = conn.execute(
        """
        SELECT * FROM books WHERE author = ?
        """, (author,)
    )
    return result.fetchall()

def delete_book_by_id(conn, book_id):
    result = conn.execute(
        """
        DELETE FROM books WHERE id = ?
        
        """, (book_id, )

    )
    conn.commit()
    return result.fetchall()


if __name__ == "__main__":
    connection = sqlite3.connect('homework_8.db')

    create_table(connection)

    books_list = [
        ('Преступление и наказание', 'Ф. Достоевский', 1866, 'Роман', 600, 5),
        ('Мастер и Маргарита', 'М. Булгаков', 1967, 'Фантастика', 480, 3),
        ('1984', 'Дж. Оруэлл', 1949, 'Антиутопия', 328, 10),
        ('Маленький принц', 'А. де Сент-Экзюпери', 1943, 'Сказка', 112, 15),
        ('Герой нашего времени', 'М. Лермонтов', 1840, 'Классика', 224, 7),
        ('Хоббит', 'Дж. Р. Р. Толкин', 1937, 'Фэнтези', 310, 12),
        ('Алхимик', 'П. Коэльо', 1988, 'Притча', 208, 8),
        ('Портрет Дориана Грея', 'О. Уайльд', 1890, 'Роман', 320, 4),
        ('Три товарища', 'Э. М. Ремарк', 1936, 'Драма', 480, 6),
        ('Автостопом по галактике', 'Д. Адамс', 1979, 'Фантастика', 224, 9)
    ]


    for book in books_list:
        insert_books(connection, *book)

    all_books = get_all_books(connection)
    for book in all_books:
        print(book)

    books_by_author = get_books_by_author(connection, "Ф. Достоевский")
    for book in books_by_author:
        print(book)

    delete_book_by_id(connection, 1)
    print("== Список после удаления ==")
    for book in get_all_books(connection):
        print(book)
    connection.close()