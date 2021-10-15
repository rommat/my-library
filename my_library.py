
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
def list_books():
    result_table = data_handler.list_all_items('book')


@cli.group()
def author():
    """ Manages authors. """


@author.command('list', help='Get list of all the authors in the library')
def list_authors():
    result_table = data_handler.list_all_items('author')
