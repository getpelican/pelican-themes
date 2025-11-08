#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Basic site information
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = 'Your site tagline'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Theme
THEME = 'graymill'

# Optional theme settings
SITE_IMAGE = 'images/share-image.jpg'  # 1200x630px for social sharing
FAVICON = 'images/favicon.png'
AVATAR = 'images/avatar.jpg'
AUTHOR_DESCRIPTION = 'Brief bio about the author'
AUTHOREMAIL = 'your.email@example.com'

# Social links (displayed in footer)
# Available icons: twitter, facebook, github, linkedin, mail, rss
SOCIAL = (
    ('twitter', 'https://twitter.com/yourusername'),
    ('github', 'https://github.com/yourusername'),
    ('linkedin', 'https://www.linkedin.com/in/yourusername'),
    ('mail', 'mailto:your.email@example.com'),
)

# Blogroll
LINKS = (
    ('Python.org', 'https://python.org/'),
    ('Pelican', 'https://getpelican.com/'),
)

# Twitter username for Twitter Card metadata
TWITTER_USERNAME = '@yourusername'

# Show social share buttons on articles
SPREAD_THE_WORD = True

# Google Analytics 4
# Format: G-XXXXXXXXXX (not the old UA-XXXXXXXXX)
GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'

# Pelican settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Feed settings
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

# Pagination
DEFAULT_PAGINATION = 10

# Development settings
RELATIVE_URLS = True
