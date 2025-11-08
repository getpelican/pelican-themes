# Graymill

A minimal, responsive theme for [Pelican](http://blog.getpelican.com/) built on [Milligram CSS](http://milligram.io/).

Version 2.1.0 | Pelican 4.0+ | MIT License

## Features

- Responsive mobile-first design
- Modern top navigation with dropdown categories
- CSS-only hamburger menu (no JavaScript)
- Automatic dark mode via `prefers-color-scheme`
- Semantic HTML5 structure
- Multiple author support
- Draft mode indicators
- JSON-LD structured data
- SVG icons
- WCAG 2.1 compliant
- CSP-ready

## Installation

Clone the repository:

```bash
git clone https://github.com/errnair/graymill.git
```

Or use pelican-themes:

```bash
pelican-themes --install graymill
```

Then set it in your `pelicanconf.py`:

```python
THEME = 'graymill'
```

## Configuration

### Required

```python
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
SITEURL = 'https://your-domain.com'
```

### Optional

```python
# Site metadata
SITEDESCRIPTION = 'Your site tagline'
AUTHOR_DESCRIPTION = 'Brief bio'
SITE_IMAGE = 'images/share-image.jpg'  # 1200x630px recommended
FAVICON = 'images/favicon.ico'
AVATAR = 'images/avatar.jpg'

# Social links (displayed in footer)
SOCIAL = (
    ('twitter', 'https://twitter.com/yourusername'),
    ('github', 'https://github.com/yourusername'),
    ('linkedin', 'https://www.linkedin.com/in/yourusername'),
)

# External links
LINKS = (
    ('Python.org', 'https://python.org/'),
    ('Pelican', 'https://getpelican.com/'),
)

# Twitter card metadata
TWITTER_USERNAME = '@yourusername'

# Show share buttons on articles
SPREAD_THE_WORD = True

# Contact email in footer
AUTHOREMAIL = 'your.email@example.com'

# Google Analytics 4
GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'
```

See `sample_pelicanconf.py` for more options.

## Article Metadata

### Images

```markdown
Title: My Article
Image: images/article-image.jpg
```

### Multiple Authors

```markdown
Title: Collaborative Post
Authors: John Doe, Jane Smith
```

### Modified Date

```markdown
Title: Updated Article
Date: 2025-01-01
Modified: 2025-01-15
```

### Draft Status

```markdown
Title: Work in Progress
Status: draft
```

### Translations

```markdown
Title: My Article
Slug: my-article
Lang: en
Translation: yes
```

## Customization

### Colors

Override CSS variables in your own stylesheet:

```css
:root {
    --color-primary: #6C7A89;
    --color-bg: #ffffff;
    --color-text: #212121;
}

@media (prefers-color-scheme: dark) {
    :root {
        --color-bg: #1a1a1a;
        --color-text: #e4e4e4;
    }
}
```

### Custom CSS

Add custom styles:

```python
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}
```

## Responsive Breakpoints

- Mobile: < 768px (hamburger menu, stacked layout)
- Tablet: 769-1024px (horizontal nav, optimized spacing)
- Desktop: > 1024px (full navigation with dropdowns)

## Security

The theme is designed with security in mind:

- No inline JavaScript or styles
- External links use `rel="noopener noreferrer"`
- URL encoding on share links
- CSP-compliant

Recommended CSP header:

```
Content-Security-Policy: default-src 'self'; script-src 'self' https://www.googletagmanager.com; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://www.google-analytics.com
```

See SECURITY.md for details.

## Migration from v1.x to v2.x

### Breaking Changes

1. **Google Analytics**: Changed from UA to GA4 format
   - Old: `GOOGLE_ANALYTICS = 'UA-XXXXXXXXX'`
   - New: `GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'`

2. **Icons**: PNG replaced with SVG
   - Old path: `/theme/images/icons/twitter.png`
   - New path: `/theme/images/icons-svg/twitter.svg`

3. **Google+**: Removed (service shutdown in 2019)

### Non-Breaking

Everything else works automatically. New features like multiple authors, modified dates, and draft mode are optional.

## Performance

- Lighthouse scores: 98+ performance, 100 accessibility
- SVG icons: 97% smaller than PNG (85KB → 2KB)
- Minimal dependencies

Browser support:
- Chrome/Edge 105+
- Firefox 121+
- Safari 16.4+

## File Structure

```
graymill/
├── LICENSE
├── README.md
├── SECURITY.md
├── sample_pelicanconf.py
├── static/
│   ├── css/
│   │   ├── custom.css
│   │   └── milligram.css
│   └── images/
│       └── icons-svg/
└── templates/
    ├── archives.html
    ├── article.html
    ├── author.html
    ├── authors.html
    ├── base.html
    ├── categories.html
    ├── category.html
    ├── index.html
    ├── page.html
    ├── pagination.html
    ├── period_archives.html
    ├── tag.html
    ├── tags.html
    └── translations.html
```

## Changelog

### v2.1.0 (January 2025)

- Modern top navigation with sticky positioning
- CSS-only hamburger menu for mobile
- Dropdown categories menu
- Footer with grid layout
- Multiple authors support
- Modified date tracking
- Draft mode with visual indicators
- JSON-LD structured data
- Mandatory Pelican templates (authors.html, period_archives.html)
- HTML validation errors fixed (unclosed tags, MIME types)
- Canonical URL implementation fixed
- Mobile navbar height issues fixed
- Undefined variable handling fixed

### v2.0.0 (January 2025)

- Semantic HTML5 elements
- SVG icons (97% file size reduction)
- Dark mode support
- Google Analytics 4
- CSP compliance
- Accessibility improvements (WCAG 2.1 AA)
- Security enhancements

### v1.0.0 (2017)

- Initial release

## Credits

- [Milligram CSS](https://milligram.io/) by CJ Patoilo
- [Feather Icons](https://feathericons.com/) (modified SVG icons)
- [Pelican](https://getpelican.com/)

## License

MIT License - see LICENSE file.

Copyright (c) 2025 Rahul Nair

## Links

- Demo: [muchBits](https://muchbits.com)
- Repository: [github.com/errnair/graymill](https://github.com/errnair/graymill)
- Issues: [github.com/errnair/graymill/issues](https://github.com/errnair/graymill/issues)

## Notes

Pelican 4.0+ required. For Pelican 3.x, use Graymill v1.0.

MIT licensed - commercial use allowed.

Social icons appear in the footer. Icon names in SOCIAL config must be lowercase and match SVG filenames.

For custom fonts, add them via custom CSS (see Customization section).

Dark mode activates automatically based on system preference. Users control this in their browser/OS settings.
