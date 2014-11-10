Syte theme for Pelican
======================

This Pelican theme is based on [Syte][syte]. It was created by [samrat][samrat], with continued development by [arnaudbos][arnaudbos].

You can [see this theme in action here][sneakernet].

![screenshot](https://raw.github.com/arnaudbos/pelican-themes/master/syte/screenshot.png)


Dependencies
------------

Pelican-Syte uses the `webassets` and `cssmin` Python packages, which can be installed via:

    pip install webassets cssmin

Also required is the [assets][] Pelican plugin, which integrates the `webassets`
package mentioned above into Pelican. Follow the instructions on the
[Pelican Plugins][] page to install the [assets][] plugin and activate it via
your settings file.


Settings
--------

This theme uses the SOCIAL setting from Pelican and build social integration on top of it with JavaScript calls.
All these settings are optional, not using them will simply not enable the social integration and the links will remain just links.

#### HTML (OPTIONAL)

* ABOUT = u'Describe yourself or your site here, this will go right under the site name'
* SITE_DESCRIPTION = u'Used in HTML meta tag for description'
* SITE_KEYWORDS = u'Used in the HTML meta tag for keywords'

#### Links

* DISPLAY_HOME_ON_MENU = True (If you still want to display a 'Home' link, note that the site name is already a link to the home page)
* GOOGLE_PLUSONE = True (If you want a Google +1 button aside the Tweet button on each article)
* CONTACT = u'your@email.com' (Pretty explicit)

#### Social integration

###### Github integration

* GITHUB_INTEGRATION_ENABLED = True (If you want to integrate Github)
* GITHUB_USERNAME = 'your_username' (Needed if GITHUB_INTEGRATION_ENABLED is set to True)

###### Google integration

* GPLUS_INTEGRATION_ENABLED = True (If you want to integrate Google+)
* GPLUS_USERNAME = 'your_username|identifier' (Needed if GPLUS_INTEGRATION_ENABLED is set to True)
* GPLUS_API_ACCESS = 'your_api_access_key' (Needed if GPLUS_INTEGRATION_ENABLED is set to True)

###### Twitter+ integration

* TWITTER_INTEGRATION_ENABLED = True (If you want to integrate Twitter)
* TWITTER_USERNAME = 'your_username' (Needed if TWITTER_INTEGRATION_ENABLED is set to True)

###### Instagram integration

* INSTAGRAM_INTEGRATION_ENABLED = True (If you want to integrate Instagram)
* INSTAGRAM_USERNAME = 'your_username' (Needed if INSTAGRAM_INTEGRATION_ENABLED is set to True)
* INSTAGRAM_API_ACCESS = 'your_api_access_key' (Needed if INSTAGRAM_INTEGRATION_ENABLED is set to True)


[syte]: http://rigoneri.github.com/syte/
[samrat]: http://samrat.github.com/
[arnaudbos]: http://github.com/arnaudbos/
[sneakernet]: http://www.sneakernet.fr/
[assets]: https://github.com/getpelican/pelican-plugins/tree/master/assets
[Pelican Plugins]: https://github.com/getpelican/pelican-plugins
