# atyna
A Pelican theme

## Features
- Responsive design.
- Jupyter notebook optimized.
- Scalable(and responsive) images optimized.
- Reading progress for articles.
- Share buttons (facebook, twiiter and Google plus)
- Google Analytics and GAUGES.
- Code Highlight Styles (github, monokai and darkly)
- Author information for articles and Author page.
- Disqus support 
- Last Read (via plugin) [soon to be implemented]


## THEME CONFIGURATIONS

#### CODE Color schemes.

Set this in pelicanconf.py:
* COLOR_SCHEME_CSS = 'github.css' 

*Other color schemes available: monokai.css and darkly.css*

#### CSS override
If you have a (self) personalized css file and would like to have that running, here's how to:

Set this in pelicanconf.py:
* CSS_OVERRIDE = ['css/mystyle.css']

#### JS Override
Set this in pelicanconf.py:
* JS_OVERRIDE = ['']

#### Cover image for Author's Page. [Relative path or an Image off the web]
Set this in pelicanconf.py:

``` AUTHORS_BIO = {
  "yourName": {
  "cover": "~/images/yourName-cover.png"
  }
}
```

#### Author Bio
Set this in pelicanconf.py:

```AUTHORS_BIO = {
  "Emmanuel": {
    "name": "Emmanuel",
    "cover": "https://iameo.github.io/downloads/images/avatar.png",
    "image": "https://iameo.github.io/downloads/images/avatar.png",
    "website": "https://iameo.github.io",
    "location": "Nigeria",
    "bio": "Write something nice about yourself or what you do (200 words MAX)"
  }
}
```

#### Web Analytics
Set this in pelicanconf.py:

* GOOGLE_ANALYTICS = "UA-XXXXX-X"
* GAUGES = "XXXXXXXX"

#### Social URLS
Set this in pelicanconf.py:
```
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))
```

#### Header Color *(This is used in place of blank Author cover image. HEX color codes allowed)*
Set this in pelicanconf.py

* HEADER_COLOR = 'black'


#### External feed URL

Add an external feed URL (e.g FeedBurner) in SOCIAL using the rss or rss-square or feed icons. A <link> tag for the external feed will be placed in <head> instead of the default Pelican feeds.


#### Sidebar Menu
Pages will be displayed here. Create your page(s) under the content/pages/ directory.

Detailed explanation here: [Pelican Doc on pages](https://docs.getpelican.com/en/3.6.3/content.html)


SCREENSHOTS:
![atyna home](https://github.com/iameo/atyna/blob/master/static/images/atyna-home-1.png)
![atyna article 1](https://github.com/iameo/atyna/blob/master/static/images/atyna-article-1.png)
![atyna article 2](https://github.com/iameo/atyna/blob/master/static/images/atyna-article-2.png)


### ACKNOWLEDGEMENT/CREDIT
- [GHOST attila](https://attila.zutrinken.com/) - Got my inspiration from here.
- [PELICAN attila](https://github.com/arulrajnet/attila-demo) - Arulrajnet made a pelican port, which served as a helper template for me.
- My Sister, Augustina. Her name is the reason why the theme is called __atyna__.


Copyright & License
[to be updated]

