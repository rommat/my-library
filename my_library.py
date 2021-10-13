
"""
    Commands

$ my-lib book list --authors
$ my-lib book get --title=<...>
                  --id=<...>
              add
              update

$ my-lib author get --all(is_flag) | --name=<...> | --books {True|False}
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


@book.command('list')
@click.option('--authors/--no-authors', default=False, help='Get author(s) of the book(s).')
def list_book(authors):
    if authors:
        data_handler.list_all_books()


@cli.group()
def author():
    """ Manages authors. """


@author.command('get')
def get_author():
    pass
