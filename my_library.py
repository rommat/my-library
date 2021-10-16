
"""
    Commands

$ my-lib book list --authors|--no-authors
$ my-lib book get --title=<...>
                  --id=<...>
              add
              update

$ my-lib author list --books|--no-books
                get
                add
                update

"""


import click
import data_handler


@click.group()
def cli():
    pass


@cli.group()
def book():
    """ Manages books. """


@book.command('list', help='Get list of all the books in the library')
@click.option('--authors/--no-authors', default=False, help='Get author(s) of the book(s).')
def list_books(authors):
    related_item = 'author' if authors else None
    result_table = data_handler.list_all_items('book', related_item)


@cli.group()
def author():
    """ Manages authors. """


@author.command('list', help='Get list of all the authors in the library')
@click.option('--books/--no-books', default=False, help='Get author(s) of the book(s).')
def list_authors(books):
    related_item = 'book' if books else None
    result_table = data_handler.list_all_items('author', related_item)
