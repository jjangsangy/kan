# -*- coding: utf-8 -*-
try:
    from unittest2 import TestCase
    import unittest2 as unittest
except ImportError:
    from unittest import TestCase
    import unittest

import os
import sys

from nose.tools import *

sys.path.insert(0, os.path.abspath('..'))

from ..structures import *

class TestStructures(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestStructures, self).__init__(*args, **kwargs)
        self.harry_potter = GoogleBooksAPIClient(
            title='Harry Potter and the Sorcerers Stone',
            author='J. K. Rowling',
            max_results=10,
            language_code='en',
            fields=('title', 'authors', 'imageLinks', 'categories', 'description'),
        )

    def test_url(self):
        base = 'https://www.googleapis.com/books/v1/volumes'
        params = [
            'q=%22intitle%3AHarry+Potter+and+the+Sorcerers+Stone%22%2B%22inauthor%3AJ.+K.+Rowling%22',
            'langRestrict=en',
            'startIndex=0',
            'maxResults=10',
            'fields=items/volumeInfo(authors,title,industryIdentifiers,title,authors,imageLinks,categories,description)',
        ]
        long_url = '?'.join([base, '&'.join(params)])
        self.assertEqual(
            self.harry_potter.url,
            long_url,
        )

    def test_json(self):
        self.assertIsInstance(self.harry_potter.json, dict)

    def test_isbn(self):
        isbn = self.harry_potter.json['items'][0]['volumeInfo']['industryIdentifiers'][-1]['identifier']
        self.assertTrue(isbn.isdigit())
        self.assertEqual(int(isbn), 9781439520031)

if __name__ == '__main__':
    unittest.main()