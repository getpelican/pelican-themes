#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'your_name'
SITENAME = 'your_website_name'
SITESUBTITLE = 'fill_me_if_you_like'
# Leave blank (like the example here below) while developing.
# Add SITEURL='https://www.your-site.com' in publishconf.py
SITEURL=''

# Path of source (ReST/Markdown) files
PATH = 'content'

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
TIMEZONE = 'UTC'

DEFAULT_LANG = 'it'
LOCALE = 'it_IT.UTF-8'

# Adds some nice effects to text
TYPOGRIFY = True

# Max words to use for summary
SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = ' …'

# web site statistics
# Matomo > 4.0 needs your Matomo installation path
# be written withour ant trailing/initial slash!
MATOMO_SSL_URL = 'your-domain.com/matomo'
MATOMO_SITE_ID = 1

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feed/all.rss.xml' # during development leave at <None>
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = 'feed/{slug}.rss.xml' # during development leave at <None>
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['assets', 'blog', 'img', 'news', 'pages']
EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/htaccess': {'path': '.htaccess'},
}

DIRECT_TEMPLATES = ['index', 'tags',  'archives', 'search', 'categories']

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}.html'
CATEGORIES_SAVE_AS = 'category.html'

DRAFT_URL = 'draft/{slug}'
DRAFT_SAVE_AS = 'draft/{slug}.html'

TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

# Author
# This is the standard Pelican structure
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
# This is a static author page
# it works only if above settings are BLANKS ('')
SINGLE_AUTHOR_SAVE_AS = 'path_to_presentation/index.html'

# In thi way all contents are created with status = draft
# unless a status = published is stated on each single content
DEFAULT_METADATA = {
   'status': 'draft',
   'author': 'your_name', # only for single auhor blog!
}

# Do not use Categories and Pages for the menu but...
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# ... list menu voices as you want
MENUITEMS = (
        ('News', '/news/'),
        ('Blog', '/blog/'),
        ('Archives', '/archives/'),
    )

###############
###         ###
### Plugins ###
###         ###
###############

PLUGIN_PATHS = [
  'plugins'
]

PLUGINS = [
  'neighbors',
  'webassets',
  'tipue_search',
  'static_comments_plus',
  'seo', # if you will use seo plugin, please keep it commented untill ready for website publication
  'sitemap',
  'readtime',
  'pelican.plugins.series',
  'pelican_tweet',
  'pelican_youtube'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

# Static comments plus
STATIC_COMMENTS_PLUS = True
STATIC_COMMENTS_DIR = 'comments'
STATIC_COMMENTS_SOURCE = 'RST'

# Twitter auth info for social_media
# fill with your Auth-keys and DO NOT share them!
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# SEO settings
#SEO_REPORT = False
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
#SEO_ARTICLES_LIMIT = 999
#SEO_PAGES_LIMIT = 999

# Readtime
READTIME_WPM = {
     'it': {
        'wpm': 190,
        'min_singular': 'minuto',
        'min_plural': 'minuti',
        'sec_singular': 'secondo',
        'sec_plural': 'secondi'
    }
}

THEME = 'themes/Z'

###############################
###                         ###
### Theme specific settings ###
###                         ###
###############################

# Import the date and extract the current year
# if you need a dynamic copyright year
from datetime import date
COPY_DATE = '2018 - '
DCOPY_DATE = date.today().year

# If set to 'True' hide the copyright
# note and shows a CC statement
CC_LICENSE = False

# Set a custom footer
# FOOTER_INCLUDE = 'your_customized_footer.html'
# IGNORE_FILES = [FOOTER_INCLUDE]
# THEME_TEMPLATES_OVERRIDE = [os.path.dirname(__file__)]

# This section let you select colors in order to override Z standard CSS colors.
# Any CSS valid properties cna be used
ACCENTS_COLOR = red
BUTTONS_BG = #000
BUTTONS_TX = #ffffff

# Set a common header for all contents
# If you do not specify a different image or
# color on each page, this one will be used
HEADER_COLOR = '#fafafa' # any CSS color is valid

# Private key of AddThis
ADDTHIS_PUBID = ''

# Show social icons in footer
SOCIAL = (('twitter', 'https://twitter.com/your_user'),
          ('github', 'https://github.com/your_user'),
          ('envelope','mailto:you@your-domain.com'))

# Color scheme for code blocks
COLOR_SCHEME_CSS = 'darkly.css'

# Customized CSS
# CSS_OVERRIDE = 'assets/css/custom.css'

# If you desire to use your own JavaScript, turn it to False
DISABLE_CUSTOM_THEME_JAVASCRIPT = True

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.with_',
    'jinja2.ext.do'
  ]
}

# custom Jinja2 filter for localizing theme
def gettext(string, lang):
    if lang == 'en':
        return string
    elif lang == 'it':
      if string == 'Archives': return 'Archivi'
      elif string == 'Archives for': return 'Archivi per'
      elif string == 'Posted by': return 'Pubblicato da'
      elif string == 'Updated on': return 'Aggiornato il'
      elif string == 'Articles by': return 'Articoli di'
      elif string == 'Authors': return 'Autori'
      elif string == 'Categories': return 'Sezioni'
      else: return string
        
JINJA_FILTERS = {
     'gettext': gettext,
     'format': lambda x, *y, **z: x.format(*y, **z)
}
