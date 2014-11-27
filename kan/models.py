# -*- coding: utf-8 -*-
from .structures import GoogleBooksAPIClient

__all__ = [
    'Book',
]

class Book(GoogleBooksAPIClient):
    """
    Front end user model

    :param title: str
    :param author: str
    :param max_results: int
    :param start_index: int
    :param language_code: str
    :param fields: tuple
    """

    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)