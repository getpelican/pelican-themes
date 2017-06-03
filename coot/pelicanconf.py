#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


SITENAME = u"c0u1d"
AUTHOR = u'c0u1d'
SITEURL = ''
#No need to define SITEURL
SITESUBTITLE = u'n0 regrets'
MENUITEMS = [('Home','/'),('Categories','/categories.html')]
COOT_HEADER_IMAGES = 'background.jpg'
#background.jpg should be placed in content/images,if you can't find a better one,you can use my background free.

COOT_FOOTER_HEADER = u'Theme Coot'
COOT_FOOTER_CONTENT = u'Coot based on framework materialize,which is fantastic!'
COPYRIGHT = u'© 2017 c0u1d'

#archives.html
COOT_ARCHIVES_HEAD_TITLE = u'Archives'
COOT_ARCHIVES_HEADER_TITLE = u'#Archives'
COOT_ACHIVES_HEADER_SUBTITLE = u'archives by c0u1d'

#author.html
#authors.html
COOT_AUTHOR_HEAD_TITLE = u'Authors'
COOT_AUTHOR_HEADER_TITLE = u'Authors'
COOT_AUTHOR_HEADER_SUBTITLE = u'Authors on c0u1d'

#categories.html
#category.html
COOT_CATEGORY_HEAD_TITLE = u'Categories'
COOT_CATEGORY_HEADER_TITLE = u'Categories'
COOT_CATEGORY_HEADER_SUBTITLE = u'Categories on c0u1d'

#index.html
COOT_INDEX_HEAD_TITLE = u'Homepage'
COOT_INDEX_HEADER_TITLE = u'c0u1d\'s Blog'
COOT_INDEX_HEADER_SUBTITLE = u'n0 regrets'

#period_archives.html
COOT_ACHIVES_CONTENT_TITLE = u'Archives'

#tag.html
COOT_TAG_HEADER_SUBTITLE = u'tag on this site'

#tags.html
COOT_TAGS_HEAD_TITLE = u'tags on this site'
COOT_TAGS_HEADER_TITLE = u'Tags'
COOT_TAGS_HEADER_SUBTITLE = u'tags on this site'

DISQUS_SITENAME = u'c0u1d'
#If you are Chinese,you should use DuoShuo:
DUOSHUO_SITENAME = u'c0u1d'


STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico' : {'path' : 'favicon.ico'}}

PATH = 'content'
THEME = '/path/to/theme/coot'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10 
#Don't use pagination patterns,it may occur BUGs!!!
#(minimum page, URL setting, SAVE_AS setting,)
#PAGINATION_PATTERNS = (
#	(1, '{base_name}/', '{base_name}/index.html'),
#	(2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
