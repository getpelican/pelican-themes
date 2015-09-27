Pelican Themes
##############

This repository contains themes for Pelican. Feel free to clone, add your own
theme, and submit a pull request. It's community-managed!

A live version can be seen at http://www.pelicanthemes.com.

Using Themes
############

These instructions assume you have already read all the `Pelican documentation`_,
have a working site, and would now like to apply a non-default theme.

.. _Pelican documentation: http://docs.getpelican.com/

First, choose a location to hold your themes. For this example, we'll use the
directory ``~/pelican-themes``, but yours could be different. Clone the
``pelican-themes`` repository to that location on your local machine:

.. code-block:: sh

	git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes

Now you should have your ``pelican-themes`` repository stored at
``~/pelican-themes/``.

To use one of the themes, edit your Pelican settings file to include this line:

.. code-block:: python

	THEME = "/home/user/pelican-themes/theme-name"

So, for instance, to use the ``mnmlist`` theme, you would edit your settings
file to include:

.. code-block:: python

	THEME = "/home/user/pelican-themes/mnmlist"

Save the changes to your settings file and then regenerate your site by using
the Makefile you should already have set up using ``pelican-quickstart``:

.. code-block:: sh

	make html

Themes can also be specified directly via the ``-t ~/pelican-themes/theme-name``
parameter to the ``pelican`` command. If you want to edit your theme, make sure
that any edits you make are made to the copy stored in
``~/pelican-themes/theme-name``. Any changes made to
files stored in your site's ``output`` directory will be deleted the next
time you generate your site.
