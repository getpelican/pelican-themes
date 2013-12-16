# pelican-bootstrap3

This is a Bootstrap 3 theme for Pelican. It's fully responsive. Bootstrap 3 has seen an official, final release now, so I don't expect any breaking changes anymore. I will try to keep it up-to-date.

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

It uses the `tag_cloud` variable for displaying tags in the sidebar. You can control the amount of tags shown with: `TAG_CLOUD_MAX_ITEMS`

Categories are disabled by default because I don't use them myself. If you want to show them in the sidebar, uncomment the relevant section in `includes/sidebar.html`

## Extras

### GitHub

The theme can show your most recently active GitHub repos in the sidebar. To enable, provide a `GITHUB_USER`. Appearance and behaviour can be controlled using the following variables:

* `GITHUB_REPO_COUNT` (default: `5`)
* `GITHUB_SKIP_FORK` (default: `False`)
* `GITHUB_SHOW_USER_LINK` (default: `True`)
* `GITHUB_SORT_ATTRIBUTE` (default: `pushed_at`, for other attributes like `stargazers_count` cf. `https://api.github.com/users/<GITHUB_USER>/repos`)
* `GITHUB_SORT_DESCENDING` (default: `True`)

### Bootswatch and other Bootstrap 3 themes

I included all the lovely Bootstrap 3 themes from [Bootswatch](http://bootswatch.com/), built by [Thomas Park](https://github.com/thomaspark). You can tell Pelican what Bootswatch theme to use, by setting `BOOTSTRAP_THEME` to the desired theme, in lowercase (ie. 'readable' or 'cosmo' etc.). My own site is using _Readable_. If you want to use any other Bootstrap 3 compatible theme, just put the minified CSS in the `static/css` directory and rename it using the following naming scheme: `bootstrap.{theme-name}.min.css`. Then update the `BOOTSTRAP_THEME` variable with the _theme-name_ used.

### AddThis

You can enable sharing buttons through [AddThis](http://www.addthis.com/) by setting `ADDTHIS_PROFILE` to your AddThis profile-id. This will display a **Tweet**, **Facebook Like** and **Google +1** button under each post.

### Facebook Open Graph

In order to make the Facebook like button work better, the template contains Open Graph metatags like `<meta property="og:type" content="article"/>`. You can disable them by setting `USE_OPEN_GRAPH` to `False`. You can use `OPEN_GRAPH_FB_APP_ID` to provide a Facebook _app id_. You can also provide a default image that will be passed to Facebook for the homepage of you site by setting `OPEN_GRAPH_IMAGE` to a relative file path, which will be prefixed by your site's static directory.

### Tag List

You can customize the separator between article tags with `TAG_LIST_SEPARATOR`. The default separator is `/`.

## Screenshot

![](screenshot.png)

![](screenshot-article.png)

## Live example

[This is my website](http://dandydev.net)
