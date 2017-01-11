#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Doe'
SITENAME = 'This is a template, replace this'
SITESUBTITLE = 'This is a template, replace this'
SITEURL = 'http://your.url'
GOOGLE_ANALYTICS = 'UA-replace-this'
DISQUS_SITENAME = 'replace-this'
AUTHOR_GITHUB = 'replace-this'
AUTHOR_TWITTER = 'replace-this'
AUTHOR_LINKEDIN = 'replace-this'
AUTHOR_EMAIL = 'replace-this@replace-this.com'
AUTHOR_SLIDESHARE = 'replace-this'
SITE_DESCRIPTION = 'This is a template, replace this'

PATH = 'content'
OUTPUT_PATH = '/YOUR_PATH'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = '/YOUR_PATH/feeds/all.atom.xml'
FEED_ALL_RSS = '/YOUR_PATH/feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/YOUR_PATH/site/theme"

PLUGIN_PATHS = ['/YOUR_PATH/site/pelican-plugins']
PLUGINS = ['pelican_dynamic']

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blogroll')

BLOG_AUTHORS = {
    'John Doe': {
        'description': """
            This is an example of description
        """,
        'short_description': """
            Data Analyst at John Doe LLC.
        """,
        'image': '../theme/images/authors/johndoe.png',
        'links': (('github', 'https://github.com/replace-this'),
                  ('twitter-square', 'https://twitter.com/replace-this')),
    }
}

BLOG_CATEGORIES = {
    'ggplot2': {
        'description': 'ggplot2 is a plotting system for R, based on the grammar of graphics, which tries to take the good parts of base and lattice graphics and none of the bad parts. It takes care of many of the fiddly details that make plotting a hassle (like drawing legends) as well as providing a powerful model of graphics that makes it easy to produce complex multi-layered graphics.',
        'thumbnail': '../theme/images/categories/ggplot2.png'
    }
}
