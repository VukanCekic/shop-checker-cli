import typer
from rich.console import Console
from rich.table import Table
from database import DatabaseInstance
from utils.book_utils import Book_Utils

console = Console()
app = typer.Typer()

DatabaseInstance.create_database()

databaseInstance = DatabaseInstance.get_instance()
databaseInstance.create_book_table()

book_utils = Book_Utils()


@app.command(short_help='Add a book to the database')
def add(name: str, category: str):
    typer.echo(f"adding book {name}, with category: {category}")
    book_utils.insert(name, category)
    show()


@app.command(short_help='Delete a book from the database')
def delete(id: int):
    typer.echo(f"trying to delete book with id of {id}")
    book_utils.delete_by_id(id)
    show()


@app.command(short_help='shows all books in the database')
def show():

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("book_id", style="dim", width=10)
    table.add_column("name", min_width=12, justify="right")
    table.add_column("category", min_width=12, justify="right")
    table.add_column("date_added", style="dim", width=20)
    res = book_utils.get_all()

    for index in range(len(res)):
        value = res[index]
        table.add_row(str(value["id"]), str(value["name"]),
                      str(value["category"]), str(value["date_added"]),
                      )
    console.print(table)


if __name__ == "__main__":
    app()
