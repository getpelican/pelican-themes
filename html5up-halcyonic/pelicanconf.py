#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Various python modules needed for the theme to function properly (specifically, jinja filters)

import sys
from datetime import datetime
sys.path.append('.')
from utils import filters

JINJA_FILTERS = { 'ordinal': filters.ordinal }
COPYRIGHT_YEAR = datetime.now().strftime('%Y')

SITENAME = 'Halcyonic'
AUTHOR = 'Pelican'
SITEDESCRIPTION = 'An HTML5 UP Theme'
SITEURL = ''
DEFAULT_DATE_FORMAT = "%B %-d, %Y"
PATH = 'content'
STATIC_PATHS = ['images']
TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Top Nav menu
MENUITEMS = (('Archives', '/archives'),
         ('Sample Page', '/sample-page'),
         ('Tags','/tags'),('Categories','/categories'),
         ('You can modify these links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'html5up-halcyonic'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors']
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
# Uncomment and edit with your GA id to enable Google Analytics
#GOOGLE_ANALYTICS = '86-7530-9'