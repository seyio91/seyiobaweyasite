#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'seyi'
SITENAME = '2nd site'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Musings of an Engineer'
SITESUBTITLE = 'Tech Lover'
SITEDESCRIPTION = 'Seyi\'s Thoughts and Attempts at Writings'
SITELOGO = SITEURL + '/images/site_logo.jpeg'

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

MAIN_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['autostatic', 'advthumbnailer']
USE_FOLDER_AS_CATEGORY = False

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

DISABLE_URL_HASH = True
SOCIAL_SHARE = True

ARTICLE_URL = 'articles/{date:%Y-%m-%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y-%m-%d}/{slug}/index.html'

SUMMARY_MAX_LENGTH = 30

PYGMENTS_STYLE = 'monokai'

DEFAULT_PAGINATION = 10

LINK_PAGINATION = True

import math, urllib.parse
JINJA_FILTERS = {
    'count_to_font_size': lambda c: '{p:.1f}%'.format(p=100 + 25 * math.log(c, 2)),
    'url_encode': lambda url: urllib.parse.quote(str(url), safe=" ")
}