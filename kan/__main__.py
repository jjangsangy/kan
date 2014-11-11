# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from argparse import ArgumentParser

from .__version__ import __version__, __release__
from .structures import *
from .models import *

__all__ = (
    'AbstractBaseAPIClient',
    'GoogleBooksAPIClient',
    'Book',
    'main',
)

def command_line():
    '''
    Parses users command line arguments and returns the namespace
    containing parsed values.
    '''
    description = 'Kan helps you find the book'
    version = ' '.join([__version__, __release__])
    parser  = ArgumentParser(prog='kan', description=description)
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % ('kan', version),
    )
    parser.add_argument(
        '--author',
        default=None,
        metavar='name',
        help='Name of the author',
    )
    parser.add_argument(
        '--max',
        type=int,
        metavar='n',
        default=10,
        choices=range(41),
        help='Maximum results to get per query: default=10, max=40',
    )
    parser.add_argument(
        '--language',
        type=str,
        metavar='code',
        default='en',
        help='Restrict the search results to those with a certain language code',
    )
    parser.add_argument(
        'title',
        help='The title of a book',
    )
    args = parser.parse_args()

    return args


def main():
    """
    Main program entry point
    """
    args = command_line()

    # TODO: Decouple Book interface and implementation
    book = Book(args.title, args.author, args.max, args.language)

    # Temporary Display Inteface
    results = book.json()['items']
    for item in results:

        info = item['volumeInfo']

        # Resolve ISBN
        if info.get('industryIdentifiers', None):
            identifier = info.get('industryIdentifiers')[0]
            isbn_id, isbn = identifier.get('type'), identifier.get('identifier')
        else:
            isbn_id, isbn = 'ISBN', 'N/A'

        # Format/Print
        display = 'Title: {title}\nAuthor: {authors}\n{isbn_id}: {isbn}\n'.format(
            title=info['title'],
            authors=', '.join(info.get('authors', ['N/A'])),
            isbn_id=isbn_id,
            isbn=isbn,
        )
        print(display)
