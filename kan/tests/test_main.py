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

from ..__main__ import *

class TestMain(unittest.TestCase):

    def test_book(self):
        pass

    def test_protocol(self):
        pass

if __name__ == '__main__':
    unittest.main()
