from distutils.log import error
import mysql.connector
from typing import List


class DatabaseInstance:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseInstance._instance == None:
            DatabaseInstance()
        return DatabaseInstance._instance

    def __init__(self,
                 user_for_db: str = "root",
                 password_for_db: str = "root",
                 database_name: str = "book_list") -> None:
        if DatabaseInstance._instance != None:
            raise Exception(
                "A Singleton cannot be instantiated multiple times")
        else:
            self.database_name = database_name
            self.connection = mysql.connector.connect(
                host="localhost",
                user=user_for_db,
                passwd=password_for_db,
                auth_plugin='mysql_native_password',
                database=database_name
            )
            DatabaseInstance._instance = self

    @staticmethod
    def create_database(
            user_for_db: str = "root",
            password_for_db: str = "root",
            database_name: str = "book_list"):

        connection = mysql.connector.connect(
            host="localhost",
            user=user_for_db,
            passwd=password_for_db,
            auth_plugin='mysql_native_password',
        )

        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

    def create_book_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(255)  NOT NULL,
            date_added DATE NOT NULL
            )""",)
