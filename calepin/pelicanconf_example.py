#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
#Adding Pelican Jinja Date Extension (https://gist.github.com/hyperking/7376940)
from datetime import datetime
import imp
jinjaext = imp.load_source('jinjaext', 'jinjaext.py')
JINJA_FILTERS = {
'convertdate': jinjaext.convertdate ,
}
CURRDATE = datetime.now()
# End of Pelican Jinja Date Extension


AUTHOR = 'J.M. Fernández'
SITENAME = 'sys$notes'
SITESUBTITLE = 'yet another personal blog'
SITEURL = 'http://fernandezcuesta.github.io'

PATH = 'content'
OUTPUT_PATH = 'fernandezcuesta.github.io/'
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".git"]

TIMEZONE = 'Europe/Madrid'
GOOGLE_ANALYTICS = ''

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TYPOGRIFY = True
DIRECT_TEMPLATES = ('index', 'archives', 'search')
WITH_FUTURE_DATES = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('google-plus', 'https://plus.google.com/+JMFernándezC'),
          ('github', 'https://github.com/fernandezcuesta/'))
SOCIAL_SQUARE_ICONS = True
ABOUT_URL = 'https://about.me/fernandez.cuesta'

DEFAULT_PAGINATION = 4

RELATIVE_URLS = True

THEME = 'calepin'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'minify']

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

SUMMARY_MAX_LENGTH = 100
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 30

#Comments
DISQUS_SITENAME = u''
DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'

#Markdown extensions: http://pythonhosted.org/Markdown/extensions/
MD_EXTENSIONS = ['codehilite(css_class=highlight, pygments_style=native)', 'extra', 'markdown.extensions.smarty']

#License
LICENSE = 'Creative Commons Attribution 4.0 International License'
LICENSE_URL = 'http://creativecommons.org/licenses/by/4.0/'
LICENSE_IMG = 'https://i.creativecommons.org/l/by/4.0/88x31.png'

#Look
USE_FAVICON = True
SITELOGO = 'title.png'
