Pelican themes
##############

This repository contains themes for Pelican. Feel free to clone, add you own
and make a pull request. It's community-managed!


How to install a new Pelican theme
##############

These instructions assume you have already completed the Pelican Quick Start 
guide at http://docs.getpelican.com/en/3.1.1/getting_started.html, have a 
working blog, and would now like to apply a non-default theme.

First, choose a directory to hold your themes.  For this example, I'll use the 
directory :code:`path_to_themes`, but yours could be different.  Then clone 
the :code:`pelican-themes` repository to your local machine.  

.. code-block:: none
	
	$ mkdir ~/path_to_themes # or whatever
	$ cd ~/path_to_themes
	$ git clone git://github.com/getpelican/pelican-themes.git
	
Now you should have your :code:`pelican-themes` repository stored at 
:code:`~/path_to_themes/pelican-themes/`.  

Next use :code:`cd` to move to the directory where you are storing your Pelican 
site.  To use one of the themes, you simply have to edit your 
:code:`pelicanconf.py` file to include this line:

.. code-block:: python

	# Add this to pelicanconf.py
	THEME = '~/path_to_themes/pelican-themes/theme_folder'

So, for instance, to use the :code:`mnmlst` theme, you would edit your config 
file to include

.. code-block:: python

	THEME = '~/path_to_themes/pelican-themes/mnmlst'

Save :code:`pelicanconf.py`.  To see the changes, regenerate your site by using 
the Makefile you should already have set up using :code:`pelican-quickstart`:

.. code-block:: none
	
	$ make html

Themes can also be specified directly using the 
:code:`pelican -t ~/path_to_themes/pelican-themes/theme_folder` option.  If you 
want to edit your theme, make sure that any edits you make are made to the copy 
stored in :code:`~/path_to_themes/pelican-themes/theme_folder`.  Any changes
made to files stored in your site's :code:`output` directory will be deleted 
the next time you generate your site.





