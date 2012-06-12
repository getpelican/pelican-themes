#Subtle
###A pelican theme

![screenshot](https://dl.dropbox.com/u/6712319/screenshot-6.png)

This is subtle, a theme for the [Pelican static site generator](http://pelican.notmyidea.org/en/2.8/index.html).
It is adapted from the [notmyidea](https://github.com/ametaireau/notmyidea) default theme. 

The social icons are from: [http://www.alexpeattie.com/projects/justvector_icons/](http://www.alexpeattie.com/projects/justvector_icons/)

The current background is from: [http://subtlepatterns.com/](http://subtlepatterns.com/)

Apart from aesthetic changes, this also adds a different set of more 'classy' social icons and icons for many more services.

If you wish to add a favicon to your website (and I believe that you should), then you should add a 16x16 icon 'favicon.ico'
file in your output directory.

*PS: I've made this documentation quite easy to follow (I hope!), computer geeks might find it too 'simplified' but hey, it's well documented*

Because this is 'based' on notmyidea (the theme), this supports all of these settings (which you would add to the pelican.conf.py file).
```
DISQUS_SITENAME	Pelican can handle disqus comments, specify the sitename you’ve filled in on disqus
```
```
GITHUB_URL	Your github URL (if you have one), it will then use it to create a github ribbon.
```
```
GOOGLE_ANALYTICS	‘UA-XXXX-YYYY’ to activate google analytics.
```
```
MENUITEMS	A list of tuples (Title, Url) for additional menu items to appear at the beginning of the main menu.
```
```
PIWIK_URL	URL to your Piwik server - without ‘http://‘ at the beginning.
```
```
PIWIK_SSL_URL	If the SSL-URL differs from the normal Piwik-URL you have to include this setting too. (optional)
```
```
PIWIK_SITE_ID	ID for the monitored website. You can find the ID in the Piwik admin interface > settings > websites.
```
```
LINKS	A list of tuples (Title, Url) for links to appear on the header.
```
```
SOCIAL	A list of tuples (Title, Url) to appear in the “social” section.
```
```
TWITTER_USERNAME	Allows to add a button on the articles to tweet about them. Add you twitter username if you want this button to appear.
```

Plus, I've added GoSquared support so their is a new command:
```
GOSQUARED_SITENAME
```

I am hoping to fork and push that to the official Pelican repository.
##Preview
[http://asselinpaul.com/](http://asselinpaul.com/)
This post might be relevant if you want to know more about my particular blog (hosting, comments): [http://asselinpaul.com/static-site.html](http://asselinpaul.com/static-site.html)

##Installation
It is easy to install this theme, just use the [pelican-themes](http://pelican.notmyidea.org/en/2.8/pelican-themes.html) command once you have downloaded the theme:
```
pelican-themes -i /path_to_theme
```
For more information about pelican-themes, [click here](http://pelican.notmyidea.org/en/2.8/pelican-themes.html).



So that every blog ain't the same (we are all unique right?), I'd appreciate two things:

* Change the background for the blog

They are some great alternatives to this pattern on [subtlepatterns.com](http://subtlepatterns.com/). To do this you would open the static folder and add your chosen pattern/background. After that you need to modify the main.css file, specificly line 21 which defines the background:
```
background: url("wavecut.png"):
```
Replace *wavecut.png* with the name of your pattern/background.

* Change the color theme
They is one main color in this theme that you can/should change to suit your liking and personality.
I'm using the #7A4700 brown, check out my site (linked in Preview) to see what elements are brown (you might have to hover over them).
To change that, I'd simply replace every value '#7A4700' in main.css by the color you want(ideally with the find and replace command).

And if you could send me a message of your blog's url, I'd love to read your great content.

##Changing Fonts

If you want to change the font for the Titles (not the one which is used for the articles), you have to change line 14 and line 42 of the file. 

At the moment, line 14 says:
```
@import url(http://fonts.googleapis.com/css?family=Lobster);
```

I'm using Google Web Fonts to get the font, here is the link to it: [Lobster](http://www.google.com/webfonts#QuickUsePlace:quickUse/Family:)

You should note that step 3 ('Add this code to your website') has multiple options. I used the @import tab to get the previous line. Choose a font and add the @import code on line 14.

On line 42, change the font-family with whatever you downloaded. In my case, it's: 
```
font-family: 'Lobster', cursive;
```

That's it, you're done. For the font that is used for the articles, do the same thing with line 15 and 22. 

##Social Icons
I've only implemented icons that I used but it's super easy to add more and best of all, the icons you are looking for are most likely already included! 

First, take a look in the main.css file. Towards line 315, you can see the social icon declaration. It looks like this:
```
.social a[href*='twitter.com'] {background-image: url('../images/icons/twitter_alt.png');
		background-size: 16px 16px;  }
```
Check to see if the one you want isn't implemented, if not, let's continue.

* open images/icon
* look for the icon you want in here or add it
* note down it's name (e.g: wikipedia.png)
* go into the main.css file and go towards line 315, you should see the icons declaration.
* copy and paste this template there:
```
.social a[href*='url_of_site'] {background-image: url('../images/icons/name_of_icon');
		background-size: 16px 16px; }
```
Change *url_of_site* with the url of the service for which you are adding an icon (e.g: wikipedia.com).
*Do not include 'www.'*

Change *name_of_icon* with the name of the icon you got in step 2 (with it's extension). In our case that is wikipedia.png .
If you icon is located somewhere else, you can also change the path but you have to make sure that I'll be included with your css.

* go into your pelican.conf.py file and add your social 'link' there(making sure that you use the correct service name and url)
For example:
```
('github', 'http://github.com/thisisalongdocumentation'),
```

You're done!

![icons](https://dl.dropbox.com/u/6712319/screenshot-5.png)
*Yeah, that is a lot of icons.*

##Notes 
I have not tested RSS and Atom feeds as I do not use these services, I think I might have removed the support for them so keep that in mind and you might be able to get the needed code on the notmyidea theme.


