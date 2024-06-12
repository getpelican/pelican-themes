#!/usr/local/bin/python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
CURRYEAR = datetime.now().strftime('%Y')

SITETITLE = 'Agency'
SITESUBTITLE = "A One Page Theme For Pelican"
SITEURL = 'https://digitalnomad.studio'
INTRO_LG = "Agency"
INTRO_SM = "A One Page Portfolio Theme For Pelican"
PORTFOLIO_TITLE = 'Portfolio'
PORTFOLIO_SUBTITLE = 'A Sample of Our Work'

THEME = '/Volumes/EXT/Projects/Agency-Pelican'
THEME_STATIC_DIR = 'assets'
PATH = 'content'
STATIC_PATHS = ['images','mail']
#STATIC_PATHS = [ 'mail','js', 'css', 'fonts']
#add images back in above

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']
DELETE_OUTPUT_DIRECTORY = True



