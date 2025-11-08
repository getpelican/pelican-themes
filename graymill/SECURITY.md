# Security

## Design Principles

Graymill is built with security as a priority:

- No inline JavaScript or styles (CSP-compliant)
- All external links use `rel="noopener noreferrer"`
- URL encoding on all user-generated content
- Semantic HTML5 with proper escaping

## Content Security Policy

The theme works with strict CSP. Recommended policy:

```
Content-Security-Policy: default-src 'self'; script-src 'self' https://www.googletagmanager.com; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://www.google-analytics.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

If you don't use Google Analytics, simplify to:

```
Content-Security-Policy: default-src 'self'; style-src 'self'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'self'
```

## XSS Protection

All user-configurable content is escaped:
- Jinja2 auto-escaping enabled
- Article titles and content use `|striptags` where needed
- Share URLs use `|urlencode`
- No `|safe` filter on user content

## Tabnabbing Prevention

External links include `rel="noopener noreferrer"`:

```html
<a href="{{link}}" target="_blank" rel="noopener noreferrer">
```

This prevents malicious sites from accessing your window object.

## Privacy

The theme respects user privacy:
- No third-party trackers (except optional Google Analytics)
- No cookies without user consent
- No fingerprinting techniques
- Social share links don't include tracking parameters

## Configuration Security

### Trusted Inputs

These config values are trusted (you control them):
- SOCIAL, LINKS, MENUITEMS
- SITEURL, SITENAME, AUTHOR

### User Content

Article metadata is properly escaped:
- Titles, tags, categories
- Author names
- Dates

### Google Analytics

If using GA4, only the measurement ID is embedded. No custom events or user data collection in the theme.

## Reporting Issues

Found a security vulnerability? Email: rn@rahul-nair.com

Please include:
- Description of the issue
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

Do not disclose publicly until patched.

## Updates

Security fixes are released as patch versions. Subscribe to GitHub releases to stay updated.
