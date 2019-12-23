PyCaxias
============

[pycaxias.org](http://pycaxias.org)

Projeto Pelican para criação so site pycaxias!

# Ambiente
```shell
git clone git@github.com:RedeNeural/PyCaxias.git;
cd PyCaxias
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Rodar
```shell
source .venv/bin/activate
invoke reserve
```

# Configuração
 - python decouple para configurar a url.

# Deploy
```shell
[dentro da env]$ invoke gh-pages
```