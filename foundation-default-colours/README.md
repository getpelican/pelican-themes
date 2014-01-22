foundation-default-colours
==========================

A pelican theme using Zurb Foundation 5 with the default colour theme. The theme is fully compatible with mobile devices (ie, menus and the display change to be mobile-friendly on small screens).

There are seven theme-specific settings you can set in your **pelicanconf.py** file (the settings shown are the defaults):

```python
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://foundation.zurb.com/">Zurb Foundation</a>. Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'monokai'
```

* If you enable `FOUNDATION_FRONT_PAGE_FULL_ARTICLES`, the front page will show full articles instead of summaries + links to the full articles.
* If you enable `FOUNDATION_ALTERNATE_FONTS`, Google Droid fonts will be used instead of the default **Open Sans** font that ships with Foundation.
* If you enable `FOUNDATION_TAGS_IN_MOBILE_SIDEBAR`, a tag list will appear in the mobile sidebar. However note that if you have a lot of tags, this list may get rather long and unweildly.
* If you wish to use the newer Google Analytics embed code, enable `FOUNDATION_NEW_ANALYTICS` and set the `FOUNDATION_ANALYTICS_DOMAIN` to the Google-Analytics-supplied name for your code block.
* If you wish to change the footer text, do so using the `FOUNDATION_FOOTER_TEXT` setting.
* Finally, you can set `FOUNDATION_PYGMENT_THEME` to any of the themes that Pygments provides:
    * autumn
    * borland
    * bw
    * colorful
    * default
    * emacs
    * friendly
    * fruity
    * manny
    * monokai
    * murphy
    * native
    * pastie
    * perldoc
    * tango
    * trac
    * vs

If you wish to enable a listing of monthly archives in the sidebar, do so by setting `MONTH_ARCHIVE_SAVE_AS` in **pelicanconf.py**. For example:

```python
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
```

On my site, I like to include centered images with small captions below them embedded throughout my posts. To do this easily, I wrote a Pelican plugin that you can access at https://github.com/FuzzyWuzzie/foundation_images. It is designed to work with this theme, usage information can be found in it's repository's README.

Enjoy!
