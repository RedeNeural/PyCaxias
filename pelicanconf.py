#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = 'Rede Neural'
SITENAME = 'PyCaxias'
SITEURL = config('SITE_URL', default='')

PATH = 'content'

PLUGIN_PATHS = ['plugins/', ]
PLUGINS=['sitemap','cname']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tags.html', 'categories.html', 'authors.html', 'archives.html']
}
ARTICLE_ORDER_BY = 'date'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('2014','#'),
    ('2015','#'),
    ('2016','#'),
    ('2018','#'),
    ('2019','#'),
)

# Social widget
SOCIAL = {
    'instagram':'',
    'twitter':'',
    'facebook':'https://www.facebook.com/pycaxias',
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True