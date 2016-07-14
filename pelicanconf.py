#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

AUTHOR = u'Jay'
SITENAME = u'Pie Thought On'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'figures', 'downloads']

NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = 'pelican-octopress-theme'
PLUGIN_PATHS = ['pelican-plugins',]
PLUGINS = [
    'summary', 
    'liquid_tags.notebook', 
#    'ga_page_view',
    ]

# Configs for pelican.plugins.ga_page_view
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# GOOGLE_SERVICE_ACCOUNT = 'jieyan8688-piethoughton@grand-master-137213.iam.gserviceaccount.com'
# GOOGLE_KEY_FILE = os.path.join(PROJECT_ROOT, 'My Project-24de0faaa3c1.pem')
# GA_START_DATE = '2016-06-01'
# GA_END_DATE = 'today'
# GA_METRIC = 'ga:pageviews'
# POPULAR_POST_COUNT = 5

SITE_UPDATED = datetime.date.today()

