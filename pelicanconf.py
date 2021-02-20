#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alephalpha0'
SITENAME = 'I caught a glimmer from the corner of my watering eye..'
SITESUBTITLE = 'Musings from a Space Cowboy.'
SITEURL = 'https://rootofpi.me'
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = True
TYPOGRIFY = True

# Source and output paths and settings.
PATH ='content/'
OUTPUT_PATH = 'output/'
PAGE_PATHS = (('pages/'),)
ARTICLE_PATHS = (('blog/'),)
#STATIC_PATHS = (('images/'),)

DEFAULT_CATEGORY = 'Blog'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d @ %H:%M'
DEFAULT_LANG = 'en'

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
         ('Neocities.org', 'https://neocities.org'),
         ('Uberspace.de', 'https://uberspace.de/en'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/replicantArray'),
          ('github', 'https://github.com/alephalpha0'),
          ('last.fm', 'https://last.fm/user/cst003'),
          ('envelope', 'mailto:dave@rootofpi.me'))

# Pagination.
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
	(1, '{base_name}/', '{base_name}/index.html'),
	(2, '{base_name}/page/{number}', '{base_name}/page/{number}/index.html'),
)

STATIC_PATHS= ['assets']

EXTRA_PATH_METADATA = {
	'assets/robots.txt': {'path': 'robots.txt'},
	'assets/favicon.ico': {'path': 'favicon.ico'}
}

# Post and Pages PATH
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category PATH
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'
AUTHORS_BIO = {
    "alephalpha0": {
        "name": "Alephalpha0",
        "cover": "/assets/images/photos/tunnelGraf.jpg",
        "image": "/assets/images/gifs/spacecowboylost.gif",
        "website": "https://rootofpi.me",
        "location": "Floating in space..",
        "bio": "A lone Space Cowboy on a mission to learn more about his reality through journaling. 36 orbits around his Sun and nature still hasn't found a way to kill him."
    }
}

### Plugins

# Sitemap
SITEMAP = {
	'format' : 'xml',
	'priorities': {
		'articles': 0.5,
		'indexes': 0.5,
		'pages': 0.5
	},
	'changefreqs': {
		'articles': 'monthly',
		'indexes': 'daily',
		'pages': 'monthly'
	}
	
}

THEME = 'atilla'

