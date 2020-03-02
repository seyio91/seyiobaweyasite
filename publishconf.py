#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.seyiobaweya.tech'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FAVICON = 'images/favicon.png'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME='www-seyiobaweya-tech'

# Following items are often useful when publishing

GOOGLE_ANALYTICS = "UA-156544577-1"
