#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic information
AUTHOR = u'author'
AUTHOREMAIL = 'myemail [at] mydomain [dot] tld'
SITENAME = u'siteName'
SITEURL = 'http://muchbits.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'
THEME = 'themes/graymill'

# Social widgets
SOCIAL = (('twitter', 'https://twitter.com/'),
          ('linkedin', 'https://www.linkedin.com/'),
          ('github', 'https://github.com/'),
          ('facebook', 'https://facebook.com/'),
         )

DEFAULT_PAGINATION = 8

SITEDESCRIPTION = 'my custom tagline/description'

# For post-summaries
DISPLAY_SUMMARY = True

# To display static pages like About, Contact etc.
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Home', SITEURL),
            )

# Feed generation is usually not desired when developing
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Favicon (path relative to './content/')
FAVICON = 'images/favicon.png'

# To include custom static files like htaccess, robots, PDF files etc. (path relative to './content/')
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
}
