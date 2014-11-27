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

    def __repr__(self):
        attributes = [
            "{0}='{1}'".format(key, value)
                for key,value in self.__dict__.items() if isinstance(value, str) and value
        ]
        return "Book({0})".format(', '.join(attributes))