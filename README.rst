This fork adds the *waterspill-en* (as seen on `this blog`_).

.. _this blog: https://dubiousdod.org/blog/

Differences from *waterspill* are:

* Language is English
* Font is larger (I have bad eyesight :) )
* Tags aren't mentioned if you have none (both at the article level and on the sidebar)
* It's possible to suppress category display
* It's possible to add custom items before/after the main menu

Example pelicanconf.py snippet:
::

    BEFORE_MENU = [
        {'name':"Main site", 'url':'/'},
    ]

    AFTER_MENU = [
        {'name':"Gallery", 'url':'http://example.com/galleries/mygallery'},
    ]

    SUPPRESS_CATEGORIES_ON_MENU = True
    SUPPRESS_ITEM_CATEGORIES = True

-------------------------------

Pelican themes
##############

This repository contains themes for pelican, feel free to clone, add you own
and make a pull request, it's community-managed!
