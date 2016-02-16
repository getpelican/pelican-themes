# [Pelican-Swain](https://github.com/FuriousSlade/pelican-swain) #
Pelican theme

Pelican 模板


>No zuo no die, why you try ?
>You zuo you die, don't ask me why.

模板用别人的总是不太爽，还是自己作死写一个吧。

基本完成。大量抄袭了[Elegant](https://github.com/talha131/pelican-elegant)，Elegant是我用过功能最全面的Pelican theme了。

## 简介 ##
使用了bootstrap3、fontawesome，评论可使用disqus或者国内的**多说**,站内搜索使用了tipuesearch。社交信息对QQ和微信做了处理：点击展示对应的二维码。

## Live demo ##
[FuriouesSlade](http://furiousslade.github.io)

## 注意事项 ##
Swain/static/images/ 目录下存放了头像、favicon.ico、QQ和微信的二维码图片。使用时请自行更换。


## Config demo ##


	# -*- coding: utf-8 -*- #
	from __future__ import unicode_literals
	
	AUTHOR = ''
	SITENAME = ''
	SITEURL = ''
	TIMEZONE = "Asia/Shanghai"
	DEFAULT_DATE_FORMAT = "%Y-%m-%d"
	
	ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'
	ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'
	PAGE_URL = 'pages/{slug}'
	PAGE_SAVE_AS = 'pages/{slug}.html'
	CATEGORY_URL = 'category/{slug}'
	CATEGORY_SAVE_AS = 'category/{slug}.html'
	TAG_URL = 'tag/{slug}.html'
	TAG_SAVE_AS = 'tag/{slug}.html'
	
	DISPLAY_CATEGORIES_ON_SIDEBAR = True
	LOAD_CONTENT_CACHE = False
	
	PATH = u'content'
	BANNER_ALL_PAGES = True
	DEFAULT_LANG = u'zh'
	FILENAME_METADATA = "(?P<slug>.*)"
	
	# Feed generation is usually not desired when developing
	FEED_ALL_ATOM = None
	CATEGORY_FEED_ATOM = None
	TRANSLATION_FEED_ATOM = None
	AUTHOR_FEED_ATOM = None
	AUTHOR_FEED_RSS = None
	
	# Blogroll
	LINKS = (('Pelican', 'http://getpelican.com/'),
	         ('Python.org', 'http://python.org/'),
	         ('Jinja2', 'http://jinja.pocoo.org/'),)
	
	# Theme
	THEME = 'pelican-swain'
	DIRECT_TEMPLATES = (
	    ('index', 'tags', 'categories', 'archives', '404', 'search'))
	
	RECENT_ARTICLES_COUNT = 10
	
	SOCIAL = (('email', 'mailto:175439093@qq.com'),
	          ('weibo', 'http://weibo.com/slade86'),
	          ('github', 'https://github.com/FuriousSlade'),
	          ('qq', '175439093'),
	          ('weixin', 'w12046'),
	          )
	          
	# projects
	PROJECTS = [{
	    'name': 'Swain',
	    'url': 'https://github.com/FuriousSlade/Swain',
	    'description': 'Pelican Theme'
	}]
	
	MD_EXTENSIONS = (['codehilite(css_class=highlight)',
	                  'extra', 'toc'])
	
	ABOUT_ME = 'I am html'
	
	DEFAULT_PAGINATION = 10

	USE_FOLDER_AS_CATEGORY = False
	
	# plugin config
	PLUGIN_PATHS = [u'./pelican-plugins']
	PLUGINS = [
	    'sitemap',
	    'gzip_cache',
	    'extract_toc',
	    'tipue_search',
	    'related_posts',
	]
	
	# relate_posts
	RELATED_POSTS_MAX = 3
	
	
	# sitemap
	SITEMAP = {
	    "format": "xml",
	    "priorities": {
	        "articles": 0.7,
	        "indexes": 0.5,
	        "pages": 0.3,
	    },
	    "changefreqs": {
	        "articles": "monthly",
	        "indexes": "daily",
	        "pages": "monthly",
	    }
	}
	
	
	# disqus
	DISQUS_SITENAME = ''
	
	# duoshuo
	DUOSHUO_SHORTNAME = ''
	
## Screenshot ##
![](https://github.com/FuriousSlade/pelican-swain/blob/master/pelican-swain-screenshot-01.png?raw=true)
![](https://github.com/FuriousSlade/pelican-swain/blob/master/pelican-swain-screenshot-02.png?raw=true)
![](https://github.com/FuriousSlade/pelican-swain/blob/master/pelican-swain-screenshot-03.png?raw=true)
