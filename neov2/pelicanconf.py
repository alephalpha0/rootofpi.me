#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'alephalpha0'
SITENAME = 'aa0.rootofpi.v2'
SITEURL = ''
LOAD_CONTENT_CACHE = False


# Source and output paths and settings.
PATH = 'content/'
OUTPUT_PATH = 'output/'
PAGE_PATHS = (('pages/'),)
ARTICLE_PATHS = (('blog/'),)
STATIC_PATHS = (('images/'),)

DEFAULT_CATEGORY = 'Blog'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d @ %H:%M'

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_MAX_ITEMS = 10
RSS_FEED_SUMMARY_ONLY = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('rootofpi.me', 'http://rootofpi.me'),
         ('Neocities.org', 'https://neocities.org'),)

# Social widget
SOCIAL = (('Twitter@ArrayReplicant', 'https://twitter.com/ArrayReplicant'),
          ('GitHub@alephalpha0', 'https://github.com/alephalpha0'),)

DEFAULT_PAGINATION = 5

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
