# -*- coding: utf-8 -*-
from .structures import GoogleBooksAPIClient

__all__ = [
    'Book',
]

class Book(GoogleBooksAPIClient):
    """
    Handles HTTP request for book.
    """

    # TODO: Handle display operations here rather than in main
    _header = ('title', 'authors', 'imageLinks', 'categories', 'description')
