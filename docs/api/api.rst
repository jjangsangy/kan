.. _api:

===================
API Module Referece
===================

Abstract base classes complement duck-typing by providing a way to define
interfaces when other techniques like ``hasattr()`` would be clumsy or subtly
wrong (for example with magic methods). ABCs introduce virtual subclasses,
which are classes that don’t inherit from a class but are still recognized
by ``isinstance()`` and ``issubclass()``; see the abc module documentation. Python
comes with many built-in ABCs for data structures
``(in the collections.abc module)``, numbers ``(in the numbers module)``, streams
``(in the io module)``, import finders and loaders ``(in the importlib.abc module)``.
You can create your own ABCs with the abc module.

==================
AbstractBaseClass
==================

Unlike Java abstract methods, these abstract methods may have an
implementation. This implementation can be called via the ``super()``
mechanism from the class that overrides it. This could be useful
as an end-point for a super-call in a framework that uses cooperative
multiple-inheritance.

.. autoclass:: kan.AbstractBaseAPIClient
    :members:


===============
Implementations
===============

.. autoclass:: kan.GoogleBooksAPIClient
    :members:

=========
Protocols
=========


.. autoclass:: kan.Book
    :members:


=========
Functions
=========

.. autofunction:: kan.main
