# -*- coding: utf-8 -*-
import json

from abc import abstractmethod, ABCMeta, abstractproperty
from contextlib import contextmanager

try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, Request, HTTPError
    from urllib import urlencode


__all__ = [
    'AbstractBaseAPIClient',
    'GoogleBooksAPIClient',
]


class AbstractBaseAPIClient:
    """
    AbstractBaseAPIClient that specifies the abstractmethods
    necessary to propertly be handled.
    The AbstractBaseClass defines a minimal set of methods that establish
    the characteristic behavior for the APIClient.

    Code that discriminates based on Abstract methods can trust that
    those methods will always be present.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def url(self):
        """
        Routes to proper destination URL and proper encoding schemes.

        :return url: str
        """
        return

    @abstractmethod
    def connect(self):
        """
        Makes connection to the backend API and handles any exceptions.
        """
        return

    @abstractmethod
    def reader(self):
        """
        Reads content.

        :return text: str
        """
        return


class GoogleBooksAPIClient(AbstractBaseAPIClient):
    """
    Implements the AbstractBaseAPIClient and talks to the google books
    api for querying and finding books.

    :return self: **GoogleBooksAPIClient<self>**
    """

    def __init__(self,
        title='',
        author='',
        max_results=10,
        start_index=0,
        language_code='',
        fields=('authors', 'title', 'industryIdentifiers'),
    ):
        """
        :param: title: str
        :param: author: str
        :param: max_results: int
        :param: start_index: int
        :param: language_code: str
        :param: fields: tuple
        """
        self.title = title
        self.author = author
        self.max_results = max_results
        self.start_index = start_index
        self.language_code = language_code
        self.fields = fields

    @property
    def url(self):
        base = r'https://www.googleapis.com/books/v1/volumes'
        query = r''

        if self.title:
            query = '"{0}"'.format(':'.join(['intitle', self.title]))
        if self.author:
            authors = '"{0}"'.format(':'.join(['inauthor', self.author]))
            query = '+'.join([query, authors]).strip('+')

        # Encode Parameters
        params = urlencode({
                       'q': query,
              'startIndex': self.start_index,
              'maxResults': self.max_results,
            'langRestrict': self.language_code,
        })

        fieldstring = 'fields={prefix}({fields})'.format(
            prefix='/'.join(['items', 'volumeInfo']),
            fields=','.join(self.fields),
        )

        return '&'.join(['?'.join([base, params]), fieldstring])

    @contextmanager
    def connect(self, agent='Python'):
        """
        Context manager for HTTP Connection state and ensures proper handling
        of network sockets, sends a GET request.

        Exception is raised at the yield statement.

        :yield request: FileIO<Socket>
        """
        headers = {'User-Agent': agent}
        request = urlopen(Request(self.url, headers=headers))
        try:
            yield request
        finally:
            request.close()

    @property
    def reader(self):
        """
        Reads raw text from the connection stream.
        Ensures proper exception handling.

        :return bytes: request
        """
        request_stream = ''
        with self.connect() as request:
            if request.msg != 'OK':
                raise HTTPError
            request_stream = request.read().decode('utf-8')
        return request_stream

    @property
    def json(self):
        """
        Serializes json text stream into python dictionary.

        :return dict: json
        """
        _json = json.loads(self.reader)
        if _json.get('error', None):
            raise HTTPError(_json['error']['errors'])
        return _json
