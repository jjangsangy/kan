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
    'command_line',
)

def command_line():
    '''
    Parses users command line arguments and returns the namespace
    containing parsed values.
    '''
    description = 'Kan helps you find the book'
    version     = ' '.join([__version__, __release__])
    parser      = ArgumentParser(prog='kan', description=description)

    subparser   = parser.add_subparsers(help='Search by')

    by_title    = subparser.add_parser('title', help='Book title',)
    by_title.add_argument('title', help='Book name')

    by_isbn     = subparser.add_parser('isbn', help='ISBN code')
    by_isbn.add_argument('code', help='Valid ISBN code')

    by_author   = subparser.add_parser('author', help='Book author')
    by_author.add_argument('author', help='Authors name')
    by_author.add_argument('--recent', help='Search by most recent', action='store_true')
    by_author.add_argument('--top', help='Search by best selling', action='store_true')

    # Main Parser
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % ('kan', version),
    )
    parser.add_argument(
        '--title',
        help='Title of the book',
        metavar='name',
    )
    parser.add_argument(
        '--author',
        default=None,
        metavar='name',
        help='Name of the author',
    )
    parser.add_argument(
        '--subject',
        type=str,
        help='Specify subject matter by category',
        metavar='topic',
    )
    parser.add_argument(
        '--max',
        type=int,
        metavar='n',
        default=3,
        choices=range(41),
        help='Maximum results to get per query: default=3, max=40',
    )
    parser.add_argument(
        '--language',
        type=str,
        metavar='code',
        default='',
        help='Restrict the search results to those with a certain language code',
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print out debug information',
    )

    return parser.parse_args()


def main():
    """
    Main program entry point
    """
    args = command_line()

    # TODO: Decouple Book interface and implementation
    query = Book(
        title=args.title,
        author=args.author,
        max_results=args.max,
        language_code=args.language,
        fields=('title', 'authors', 'imageLinks', 'categories', 'description'),
    )

    if args.verbose:
        print('Request URL:')
        print(query.url)
        print(query.__dict__)

    # Temporary Display Interface
    books = query.json.get('items', None)
    if not books:
        raise AttributeError('Web Request Failed')

    for book in books:
        info = book['volumeInfo']

        # Retrieve ISBN/Reference Info
        if 'industryIdentifiers' in info:
            identifiers = dict([(ref['type'], ref['identifier']) for ref in info['industryIdentifiers']])

            # Prefer ISBN 13 over ISBN 10
            if 'ISBN_13' in identifiers:
                isbn_id, isbn = 'ISBN_13', identifiers['ISBN_13']
            else:
                isbn_id, isbn = identifiers.popitem()

        else:
            isbn_id, isbn = 'ISBN_##', 'N/A'

        # Format/Print
        display = 'Title: {title}\nAuthor: {authors}\n{isbn_id}: {isbn}\n'.format(
            title=info['title'],
            authors=', '.join(info.get('authors', ['N/A'])),
            isbn_id=isbn_id,
            isbn=isbn,
        )

        print(display)
