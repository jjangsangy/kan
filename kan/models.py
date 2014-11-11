# -*- coding: utf-8 -*-
import json

from structures import GoogleBookAPIClient

__all__ = [
    'Book',
]

class Book:
    """
    Handles HTTP request for book.
    """

    _header = ('title', 'authors', 'imageLinks', 'categories', 'description')

    def __init__(self, title, author=None, header=_header):
        """
        :param title: string
        :param header: string
        :param interface: **Implementation<AbstractBaseAPIClient>**
        """
        self.title = title
        self.header = header
        self.implementation = GoogleBookAPIClient(title, author=author)

    def json(self):
        """
        :return dict: json
        """
        raw_text = self.implementation.reader()
        return json.loads(raw_text)
