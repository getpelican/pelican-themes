#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# top-right corner in navbar
AUTHOR = 'Zahar Celac'
LINKEDIN_URL = 'https://linkedin.com/in/zaharcelac'

# top-left icon/brand
SITENAME_HTML = '<i class="fa fa-universal-access fa-lg"></i>'

# title
SITENAME = 'Notes'

# footer text
CC = "This work is licensed under a <a href='https://creativecommons.org/licenses/by/4.0/' target='_blank' title='Creative Commons Attribution 4.0 International License'>CC BY 4.0</a>."
CREDITS =  "Powered by <a href='https://github.com/getpelican' target='_blank'>pelican</a> and <a href='#' target='_blank'>personal-bootstrap4</a>."

SITEURL = 'http://localhost'
PATH = './content'
THEME = './theme'
STATIC_PATHS = ['images']

USE_FOLDER_AS_CATEGORY = True
CHECK_MODIFIED_METHOD = 'mtime'
TIMEZONE = 'America/NewYork'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = 3
SUMMARY_MAX_LENGTH = None
LOAD_CONTENT_CACHE = False

# navbar content
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAG_LINK_ON_MENU = True

# code highlight
PYGMENTS_STYLE = 'monokai'
MARKDOWN_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']
TYPOGRIFY = True

# disabling other content
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
AUTHOR_SAVE_AS = False
