# pelican-bootstrap3

This is a Bootstrap 3 theme for Pelican. It's fully responsive. Bootstrap 3 has seen an official, final release now, so I don't expect any breaking changes anymore. I will try to keep it up-to-date.

## NOTE

If you want to adjust this theme to your own liking, I encourage you to fork it. This theme has started to gather more and more attention in the form of stars and forks. I'm not seeing much real participation though :) If you make improvements that are useful to others and can make the theme better in general **please don't hesitate to make a pull request**.

## Installation

First:

`git clone https://github.com/DandyDev/pelican-bootstrap3.git`

Then:

Point the `THEME` variable in your `pelicanconf.py` to `/path/to/pelican-bootstrap3`

## Usage

This theme honors the following standard Pelican settings:

* Putting feeds in the `<head>` section:
	* `FEED_ALL_ATOM`
	* `FEED_ALL_RSS`
* Template settings:
	* `DISPLAY_PAGES_ON_MENU`
	* `DISPLAY_CATEGORIES_ON_MENU`
	* `MENUITEMS`
* Analytics & Comments
	* `GOOGLE_ANALYTICS`
	* `DISQUS_SITENAME`
	* `PIWIK_URL`, `PIWIK_SSL_URL` and `PIWIK_SITE_ID`

It uses the `tag_cloud` variable for displaying tags in the sidebar. You can control the amount of tags shown with: `TAG_CLOUD_MAX_ITEMS`

## Extras

### Sidebar options

The following things can be displayed on the sidebar:

* **Social links** can be provided through the `SOCIAL` variable. If it's empty, the section will not be shown
	* In your `pelicanconf.py` provide your social links like this:

```
SOCIAL = (('twitter', 'http://twitter.com/DaanDebie'),
          ('linkedin', 'http://www.linkedin.com/in/danieldebie'),
          ('github', 'http://github.com/DandyDev'),)
```
* **Tags** will be shown if `DISPLAY_TAGS_ON_SIDEBAR` is set to _True_
* **Categories** will be shown if `DISPLAY_CATEGORIES_ON_SIDEBAR` is set to _True_
* **Recent Posts** will be shown if `DISPLAY_RECENT_POSTS_ON_SIDEBAR` is set to _True_
	* Use `RECENT_POST_COUNT` to control the amount of recent posts. Defaults to **5**

### reStructuredText styles

If you're using reStructuredText for writing articles and pages, you can include the extra CSS styles that are used by the `docutils`-generated HTML by setting `DOCUTIL_CSS` to True. This can be done as a global setting or  setting it in the metadata of a specific article or page.

### GitHub

The theme can show your most recently active GitHub repos in the sidebar. To enable, provide a `GITHUB_USER`. Appearance and behaviour can be controlled using the following variables:

* `GITHUB_REPO_COUNT`
* `GITHUB_SKIP_FORK`
* `GITHUB_SHOW_USER_LINK`

### Bootswatch and other Bootstrap 3 themes

I included all the lovely Bootstrap 3 themes from [Bootswatch](http://bootswatch.com/), built by [Thomas Park](https://github.com/thomaspark). You can tell Pelican what Bootswatch theme to use, by setting `BOOTSTRAP_THEME` to the desired theme, in lowercase (ie. 'readable' or 'cosmo' etc.). My own site is using _Readable_. If you want to use any other Bootstrap 3 compatible theme, just put the minified CSS in the `static/css` directory and rename it using the following naming scheme: `bootstrap.{theme-name}.min.css`. Then update the `BOOTSTRAP_THEME` variable with the _theme-name_ used.

#### Update: Readable has seen some major changes. I added the new version as 'readable' and renamed the old version to 'readable-old'. Update your config accordingly.

### AddThis

You can enable sharing buttons through [AddThis](http://www.addthis.com/) by setting `ADDTHIS_PROFILE` to your AddThis profile-id. This will display a **Tweet**, **Facebook Like** and **Google +1** button under each post.

### Facebook Open Graph

In order to make the Facebook like button work better, the template contains Open Graph metatags like `<meta property="og:type" content="article"/>`. You can disable them by setting `USE_OPEN_GRAPH` to `False`. You can use `OPEN_GRAPH_FB_APP_ID` to provide a Facebook _app id_. You can also provide a default image that will be passed to Facebook for the homepage of you site by setting `OPEN_GRAPH_IMAGE` to a relative file path, which will be prefixed by your site's static directory.

### Footer

The footer will display a copyright message using the AUTHOR variable and the year of the latest post.

## Screenshot

![](screenshot.png)

![](screenshot-article.png)

## Live example

[This is my website](http://dandydev.net)