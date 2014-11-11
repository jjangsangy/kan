# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from argparse import ArgumentParser

from .__version__ import __version__, __release__
from .structures import *
from .models import *

__all__ = (
    'AbstractBaseAPIClient',
    'GoogleBookAPIClient',
    'Book',
    'main',
)

def command_line():
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
        help='Book Author',
    )
    parser.add_argument(
        'title',
        help='The title of a book',
    )

    args = parser.parse_args()

    return args


def main():
    """
    Ad Hoc Argument Parser
    """
    parse = command_line()
    book = Book(parse.title, parse.author)
    results = book.json()['items']
    for item in results:
        print(item['volumeInfo']['title'])
