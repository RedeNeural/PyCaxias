# -*- coding: utf-8 -*-
"""Tarefas de build do site do PyCaxias.

    invoke serve     -> sobe o site em http://localhost:8000 com autoreload
    invoke build     -> gera o site em output/
    invoke publish   -> gera com as URLs de producao
    invoke clean     -> apaga output/
    invoke to-old    -> gera o snapshot estatico do ano atual em old/{SITEYEAR}/
    invoke gh-pages  -> publica no branch gh-pages
"""

import datetime
import os
import shutil

from invoke import task

from pelicanconf import OLD_EVENTS, SITEYEAR

CONFIG = {
    'settings_base': 'pelicanconf.py',
    'settings_publish': 'publishconf.py',
    'deploy_path': 'output',
    'github_pages_branch': 'gh-pages',
    'commit_message': "Publica o site em {}".format(datetime.date.today().isoformat()),
    'port': 8000,
    'host': 'localhost',
}


def _move_old_to_output():
    """Copia os snapshots de old/{ano}/ para dentro de output/{ano}/."""
    for ano, _url in OLD_EVENTS:
        origem = os.path.join('old', ano)
        destino = os.path.join(CONFIG['deploy_path'], ano)
        if not os.path.isdir(origem):
            continue
        if os.path.isdir(destino):
            shutil.rmtree(destino)
        shutil.copytree(origem, destino)


def _move_cname():
    shutil.copy('CNAME', os.path.join(CONFIG['deploy_path'], 'CNAME'))


@task
def clean(c):
    """Apaga o diretorio de saida."""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])


@task
def build(c):
    """Gera o site."""
    c.run('pelican content -s {settings_base} -o {deploy_path}'.format(**CONFIG))
    _move_old_to_output()
    _move_cname()


@task
def rebuild(c):
    """Apaga tudo e gera de novo."""
    clean(c)
    build(c)


@task
def publish(c):
    """Gera o site com as configuracoes de producao."""
    c.run('pelican content -s {settings_publish} -o {deploy_path}'.format(**CONFIG))
    _move_old_to_output()
    _move_cname()


@task
def serve(c):
    """Sobe um servidor local que recarrega ao salvar arquivos."""
    from livereload import Server

    def recarregar():
        clean(c)
        build(c)

    recarregar()

    servidor = Server()
    servidor.watch('pelicanconf.py', recarregar)
    servidor.watch('content/**/*.md', recarregar)
    servidor.watch('theme/templates/**/*.html', recarregar)
    servidor.watch('theme/static/**/*', recarregar)

    print('\n  PyCaxias rodando em http://{host}:{port}\n'.format(**CONFIG))
    servidor.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def to_old(c):
    """Gera o snapshot estatico do ano atual (SITEYEAR) em old/{ano}/."""
    folder = 'old/{}/'.format(SITEYEAR)
    c.run('pelican content -s {settings_base} -o {folder}'.format(folder=folder, **CONFIG))


@task
def gh_pages(c):
    """Publica o conteudo de output/ no branch gh-pages."""
    publish(c)
    c.run(
        'ghp-import -b {github_pages_branch} -m "{commit_message}" '
        '-p {deploy_path} -n'.format(**CONFIG)
    )
