#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = 'Rede Neural'

SITENAME = 'PyCaxias 2023'
SITEYEAR = 2023

SITEURL = config('SITE_URL', default='/')

PATH = 'content'

PLUGIN_PATHS = ['plugins/', ]
PLUGINS=['sitemap',]

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

# OLD_EVENTS
OLD_EVENTS = (
    ('2014','/2014'),
    ('2015','/2015'),
    ('2016','/2016'),
    ('2018','/2018'),
    ('2020','/2020'),
    ('2022','/2022'),
)
# OLD_EVENTS
MENU = (
    ('#intro','Início', True),
    ('#about','Sobre', False),
    ('#schedule','Agenda', False),
    ('#inscricao','Inscrição', False),
    ('#supporters','Patrocinadores', False),
    ('#contact','Contato', False),
)

INSCRICAO_LINK = 'https://www.sympla.com.br/pycaxias-2023__1873136?share_id=5rmrc'

# Social widget
SOCIAL = {
    'instagram':'https://www.instagram.com/pycaxias',
    'twitter':'',
    'facebook':'https://www.facebook.com/pycaxias',
}

DEFAULT_PAGINATION = False
SITE_META_KEYWORDS = "PyCaxias 2020, evento python, caxias do sul, evento caxias do sul, python, pycaxias, comunidade python caxias do sul, python rio grande do sul, comunidade"
SITE_META_DESCRIPTION = "Evento da comunidade Python de Caxias do Sul, com intuito de popularizar e disseminar o conhecimento da linguagem python"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True