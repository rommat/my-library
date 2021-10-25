
"""
    Commands
"""


import click
import command_execution as exec


@click.group()
def cli():
    pass


@cli.group()
def book():
    """ Manages books. """


@book.command('list', help='Get list of all the books in the library.')
@click.option('--authors/--no-authors', default=False, help='Get author(s) of the book(s).')
def list_books(authors):
    exec.book_list(authors)


@book.command('get', help='Get information about the book.')
@click.option('--id', 'book_id', type=int, help='ID of the book.')
@click.option('--title', help='Title of the book. It will be ignored if ID is present')
@click.option('--authors/--no-authors', default=False, help='Get author(s) of the book.')
def get_book(book_id, title, authors):
    if book_id:
        parameters = {'id': book_id}
    elif title:
        parameters = {'title': title}
    else:
        raise ValueError
    exec.book_get(parameters, authors)


@cli.group()
def author():
    """ Manages authors. """


@author.command('list', help='Get list of all the authors in the library')
@click.option('--books/--no-books', default=False, help='Get author(s) of the book(s).')
def list_authors(books):
    exec.author_list(books)


@author.command('get', help='Get information about the author.')
@click.option('--id', 'author_id', type=int, help='ID of the book.')
@click.option('--first-name', help='Required "last-name" to be entered.')
@click.option('--last-name', help='Required "first-name" to be entered.')
@click.option('--books/--no-books', default=False, help='Get author(s) of the book(s).')
def get_author(author_id, first_name, last_name, books):
    if author_id:
        parameters = {'id': author_id}
    elif first_name and last_name:
        parameters = {'first_name': first_name, 'last_name': last_name}
    else:
        raise ValueError
    exec.author_get(parameters, books)
