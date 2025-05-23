#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = 'Rede Neural'

SITENAME = 'PyCaxias 2025'
SITEYEAR = 2025
DAY_EVENT = "17 de Maio de 2025"
DAY_EVENT_SHORT = "17/05/2025"
LOCAL = "UCS, Bloco J"
CALL_FOR_PAPERS = "https://forms.gle/mcw6gjmCjzu8cnN9A"
INCRICAO_OPENED = True
INSCRICAO_LINK = 'https://www.sympla.com.br/evento/pycaxias-2025/2804197'

SITEURL = config('SITE_URL', default='/')

PATH = 'content'

SITEMAP = {
    'format': 'xml',
    'exclude': ['tags.html', 'categories.html', 'authors.html', 'archives.html']
}

ARTICLE_ORDER_BY = 'date'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# OLD_EVENTS
OLD_EVENTS = (
    ('2014','/2014'),
    ('2015','/2015'),
    ('2016','/2016'),
    ('2018','/2018'),
    ('2020','/2020'),
    ('2022','/2022'),
    ('2023','/2023'),
    ('2024','/2024'),
)
# OLD_EVENTS
MENU = (
    ('#intro','Início', True),
    ('#about','Sobre', False),
    ('#schedule','Agenda', False),
    ('#supporters','Patrocinadores', False),
    ('#contact','Contato', False),
)

# Social widget
SOCIAL = {
    'instagram':'https://www.instagram.com/pycaxias',
    'twitter':'',
    'facebook':'https://www.facebook.com/pycaxias',
}

DEFAULT_PAGINATION = False
SITE_META_KEYWORDS = "PyCaxias 2025, evento python, caxias do sul, evento caxias do sul, python, pycaxias, comunidade python caxias do sul, python rio grande do sul, comunidade"
SITE_META_DESCRIPTION = "Evento da comunidade Python de Caxias do Sul, com intuito de popularizar e disseminar o conhecimento da linguagem python"
SITE_V=1
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True