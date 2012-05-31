
# SVBTLE

Svbtle theme is a close copy of [Svbtle.com](http://www.svbtle.com) with a few minor changes for use with [Pelican](http://pelican.notmyidea.org).

## DEMO

You can see the theme in action in this blog [post](http://williamting.com/drafts/this-is-a-theme-testing-post.html). The theme code is available [here](https://github.com/wting/pelican-svbtle), or the website code [here](https://github.com/wting/williamting.com).

![theme screenshot](https://raw.github.com/wting/pelican-svbtle/master/screenshot.png)

## FEATURES

- syntax highlighting for code blocks
- Google Analytics
- Disqus commenting
- custom list of links

## KNOWN ISSUES

- no pages feature
- no custom menu
- header date format is hardcoded in `./templates/header.html` with the exception of articles which uses `DEFAULT_DATE_FORMAT`

## INSTALL

### FROM SOURCE

Download the [repository](https://github.com/wting/pelican-svbtle) and save it somewhere accessible. Edit `settings.py` and modify the `THEME` variable to point to the downloaded theme location.

### FROM OFFICIAL REPO

Please refer to Pelican theme [install instructions](http://pelican.notmyidea.org/en/latest/pelican-themes.html).

## SETTINGS.PY

These are the Pelican global variables currently supported by the theme:

- `GOOGLE_ANALYTICS`
- `DISQUS_SITENAME`
- `LINKS(('name1', 'url1'), ('name2', 'url2'))`
- `DEFAULT_DATE_FORMAT = ('%b %d, %Y')`: suggested date format
- `FEED_DOMAIN = SITEURL`

## MODIFICATION

- Accent color can be changed by editing `@accent` in `./static/css/style.less`.

- A different Pygmentize theme can be used by editing `./Makefile` and running `make pygments`.

## AUTHOR

William Ting

## LICENSE

Released under MIT License, full details in `LICENSE` file.
