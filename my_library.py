
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
import data_handler as dh
import output_processing as out


@click.group()
def cli():
    pass


@cli.group()
def book():
    """ Manages books. """


@book.command('list', help='Get list of all the books in the library.')
@click.option('--authors/--no-authors', default=False, help='Get author(s) of the book(s).')
def list_books(authors):
    related_item = 'author' if authors else None
    result_table = dh.list_all_items('book', related_item)
    out.table2console(result_table)


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
    related_item = 'author' if authors else None
    result = dh.get_item('book', parameters, related_item)
    out.row2console(result)


@cli.group()
def author():
    """ Manages authors. """


@author.command('list', help='Get list of all the authors in the library')
@click.option('--books/--no-books', default=False, help='Get author(s) of the book(s).')
def list_authors(books):
    related_item = 'book' if books else None
    result_table = dh.list_all_items('author', related_item)
    out.table2console(result_table)
