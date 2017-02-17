======
TuitFS
======

This is the quick-and-dirty Python library and GTK+ client for TuitFS, the storage system which
relies on Twitter as its (default) infrastructure. It also acts as a primitive version control system.

Currently, the package depends on GTK+ and displays a GUI whenever executed, but in the future
this behavior will be replaced, and instead a console interface will be available too. The user interface will be determined by either environmental values (such as DISPLAY?) or a command option.
The package should also be problably split into two, library and user interface. But not for now :3

.. contents::

-----
Setup
-----

Installing TuitFS is a straight-forward process:

::

	$ ./setup.py build
	$ sudo ./setup.py install

.. include:: specs.rst
