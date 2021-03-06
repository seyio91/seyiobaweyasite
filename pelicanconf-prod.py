#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Seyi Obaweya'
SITENAME = 'Seyi\'s Tech Blog'
SITEURL = 'https://www.seyiobaweya.tech'
SITETITLE = 'Musings of an Engineer'
SITESUBTITLE = 'Tech Lover'
SITEDESCRIPTION = 'Seyi\'s Thoughts and Attempts at Writings'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'Flex'
STATIC_PATHS = ['images', 'static']
# FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'

# Blogroll
# LINKS = (('Portfolio', 'http://alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/obaweya-seyi-375270ba'),
          ('github', 'https://github.com/seyio91'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['autostatic', 'advthumbnailer']
USE_FOLDER_AS_CATEGORY = False

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

DISABLE_URL_HASH = True

ARTICLE_URL = 'articles/{date:%Y-%m-%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y-%m-%d}/{slug}/index.html'


SUMMARY_MAX_LENGTH = 30

PYGMENTS_STYLE = 'monokai'
