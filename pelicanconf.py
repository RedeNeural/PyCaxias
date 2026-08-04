#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from decouple import config

# ---------------------------------------------------------------------------
# Identidade do evento
# Tudo que muda de um ano para o outro esta aqui. O tema le estes valores.
# ---------------------------------------------------------------------------
AUTHOR = 'Rede Neural'

SITENAME = 'PyCaxias 2026'
SITEYEAR = 2026

DAY_EVENT = '26 de setembro de 2026'
DAY_EVENT_SHORT = '26/09/2026'
DAY_EVENT_ISO = '2026-09-26T08:00:00-03:00'   # usado na contagem regressiva
WEEKDAY_EVENT = 'Sábado'
HOURS_EVENT = '08h às 18h'

LOCAL = 'Uniftec Caxias do Sul'
LOCAL_ADDRESS = 'Rua Ludovico Cavinato, 2570 - Bairro Fátima, Caxias do Sul/RS'
LOCAL_MAP = 'https://www.google.com/maps/search/?api=1&query=Uniftec+Caxias+do+Sul'

# Chamadas e inscricoes
CALL_FOR_PAPERS = 'https://docs.google.com/forms/d/e/1FAIpQLScD8pNEFKBdWY22R0jzD3ItPMHs8YQtBxLpYJw-Wb1W1Of2ZA/viewform?pli=1'
CALL_FOR_PAPERS_OPENED = True
INCRICAO_OPENED = True
INSCRICAO_LINK = 'https://www.sympla.com.br/evento/pycaxias-2026/3508411'
INSCRICAO_TSHIRT_DEADLINE = ''

# ---------------------------------------------------------------------------
# Pelican
# ---------------------------------------------------------------------------
SITEURL = config('SITE_URL', default='')

PATH = 'content'
THEME = 'theme'
OUTPUT_PATH = 'output'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-br'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

ARTICLE_ORDER_BY = 'date'
DEFAULT_PAGINATION = False

ARTICLE_URL = 'palestra/{slug}/'
ARTICLE_SAVE_AS = 'palestra/{slug}/index.html'

DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {}

# ---------------------------------------------------------------------------
# Navegacao
# ---------------------------------------------------------------------------
MENU = (
    ('#sobre', 'Sobre'),
    ('#agenda', 'Agenda'),
    ('#palestrantes', 'Palestrantes'),
    ('#inscricao', 'Inscrição'),
    ('#patrocinio', 'Patrocínio'),
    ('#contato', 'Contato'),
)

OLD_EVENTS = (
    ('2014', '/2014'),
    ('2015', '/2015'),
    ('2016', '/2016'),
    ('2018', '/2018'),
    ('2020', '/2020'),
    ('2022', '/2022'),
    ('2023', '/2023'),
    ('2024', '/2024'),
    ('2025', '/2025'),
)

# ---------------------------------------------------------------------------
# Contato e redes
# ---------------------------------------------------------------------------
EMAIL = 'pythoncaxias@gmail.com'

CONTATOS = (
    {
        'nome': 'Lucas Eduardo',
        'papel': 'Organização e patrocínio',
        'telefone': '(54) 9 9124-6539',
        'whatsapp': 'https://api.whatsapp.com/send?phone=5554991246539&text=Ola%20Lucas,%20gostaria%20de%20falar%20sobre%20o%20PyCaxias',
        'telegram': 'https://t.me/LucasEduard',
    },
    {
        'nome': 'Pedro',
        'papel': 'Organização',
        'telefone': '(54) 9 9170-9966',
        'whatsapp': 'https://api.whatsapp.com/send?phone=5554991709966&text=Ola%20Pedro,%20gostaria%20de%20falar%20sobre%20o%20PyCaxias',
        'telegram': '',
    },
)

SOCIAL = {
    'instagram': 'https://www.instagram.com/pycaxias',
    'facebook': 'https://www.facebook.com/pycaxias',
    'github': 'https://github.com/RedeNeural/PyCaxias',
    'twitter': '',
}

CODIGO_CONDUTA = 'https://python.org.br/cdc/'

# ---------------------------------------------------------------------------
# SEO
# ---------------------------------------------------------------------------
SITE_META_DESCRIPTION = (
    'PyCaxias 2026: um sábado inteiro de Python na Serra Gaúcha. '
    '26 de setembro, na Uniftec Caxias do Sul. Entrada gratuita.'
)
SITE_META_KEYWORDS = (
    'PyCaxias 2026, evento python, caxias do sul, python, comunidade python, '
    'serra gaúcha, uniftec, evento de tecnologia caxias do sul, python brasil'
)
SITE_V = '2026.1'

GA_ID = 'GTM-MPWH9CMP'

# RELATIVE_URLS = True
