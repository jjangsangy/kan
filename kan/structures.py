# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta
from contextlib import contextmanager

try:
    from urllib.request import urlopen, Request, quote
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import urlopen, Request, quote
    from urllib import urlencode


__all__ = [
    'AbstractBaseAPIClient',
    'GoogleBookAPIClient',
]

class AbstractBaseAPIClient:
    """
    AbstractBaseAPIClient that specifies the abstractmethods
    necessary to propertly be handled.
    Unlike Java's abstract methods or C++'s pure abstract methods,
    abstract methods as defined here may have an implementation.
    In addition, the ABCs define a minimal set of methods that establish
    the characteristic behavior of the type.

    Code that discriminates objects based on their ABC type can trust that
    those methods will always be present.
    """
    __metaclass__ = ABCMeta
    @abstractmethod
    def connect():
        pass
    @abstractmethod
    def reader():
        pass

class GoogleBookAPIClient(AbstractBaseAPIClient):
    """
    Implements the AbstractBaseAPIClient and talks to the google books
    api for querying and finding books.

    :return self: **GoogleBookAPIClient<self>**
    """

    def __init__(self, title, author=None):
        """
        :param title: str
        """
        self.title = title
        self.author = author

    @property
    def url(self):
        base = r'https://www.googleapis.com/books/v1/volumes'
        query = r'"{title}"'.format(title=self.title)
        if self.author:
            query = ' '.join([query, ':'.join(['inauthor', self.author])])
        params = urlencode({
            'q': query,
            'maxResults': 10,
            })
        url = '?'.join([base, params])
        return url

    @contextmanager
    def connect(self):
        """
        Context manager for HTTP Connection state and ensures proper handling
        of network sockets, sends a GET request.

        Exception is raised at the yield statement.

        :yield request: FileIO<Socket>
        """
        try:
            headers = {'User-Agent': 'Python'}
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
                raise IOError
            request_stream = request.read().decode('utf-8')
        return request_stream
