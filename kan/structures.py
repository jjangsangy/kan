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

    def __init__(self, title,
                 author=None,
                 max_results=10,
                 start_index=1,
                 language_code='en'
                 ):
        """
        :param title: str

        :param author: str
        :param max_results: int
        :param start_index: int
        :param lang: str
        """
        self.title = title
        self.author = author
        self.max_results = max_results
        self.start_index = start_index
        self.language_code = language_code

    @property
    def url(self):
        base = r'https://www.googleapis.com/books/v1/volumes'
        query = r'"{title}"'.format(title=self.title)

        # API parameterizes author within query string.
        if self.author:
            authors = ':'.join(['inauthor', self.author])
            query = ' '.join([query, authors])

        # Encode Parameters
        params = urlencode({
            'q': query,
            'maxResults': self.max_results,
            'langRestrict': self.language_code,
        })

        return '?'.join([base, params])

    @contextmanager
    def connect(self, agent='Python'):
        """
        Context manager for HTTP Connection state and ensures proper handling
        of network sockets, sends a GET request.

        Exception is raised at the yield statement.

        :yield request: FileIO<Socket>
        """
        try:
            headers = {'User-Agent': agent}
            request = urlopen(Request(self.url, headers=headers))
            yield request
        finally:
            request.close()

    def reader(self):
        """
        Reads raw text from the connection stream.
        Ensures proper exception handling.

        :return bytes: request
        """
        with self.connect() as request:
            if request.msg != 'OK':
                raise HTTPError
            request_stream = request.read().decode('utf-8')
        return request_stream

    def json(self):
        """
        :return dict: json
        """
        raw_text = self.reader()
        return json.loads(raw_text)
