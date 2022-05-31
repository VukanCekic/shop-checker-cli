

from database import DatabaseInstance
from models.book import Book
from datetime import datetime


class Book_Utils:

    def __init__(self):
        self.database = DatabaseInstance.get_instance()

    def insert(self, name, category):
        cursor = self.database.connection.cursor()
        sql = (

            "INSERT INTO books(name, category, date_added)"
            "VALUES (%s, %s, %s)"
        )
        data = (name, category,
                datetime.today().strftime('%Y-%m-%d'),)
        cursor.execute(sql, data)
        self.database.connection.commit()

        cursor.close()

    def delete_by_id(self, id):
        cursor = self.database.connection.cursor()
        sql = "DELETE FROM books WHERE id = %s"
        data = (id,)
        try:
            cursor.execute(sql, data)
            self.database.connection.commit()
        except:
            self.database.connection.rollback()
        finally:
            cursor.close()

    def get_all(self):
        cursor = self.database.connection.cursor()
        cursor.execute(
            f'SELECT * FROM books')
        results = cursor.fetchall()

        books = []
        for result in results:
            books.append(Book(*result))

        cursor.close()
        return books
