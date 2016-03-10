# Octofiles

[![Build Status](https://travis-ci.org/hackultura/octofiles.png?branch=master)](https://travis-ci.org/hackultura/octofiles)

Serviço de armazenamento de documentos dos entes artísticos, acessado pela plataforma SISCULT.

## Requerimentos Básicos

Você precisa:

 - Python 2.7 ou 3.2+
 - virtualenv
 - Git
 - PostgreSQL
 - Redis

## Instalação

Faça o checkout do projeto:

```bash
$ git clone https://github.com/gilsondev/octofiles.git
```

Crie o ambiente virtual:

```bash
$ cd octofiles
$ virtualenv venv
$ source bin/active
```

Instale as dependências:

```bash
$ pip install -r requirements.txt
```

Rode o servidor local:

```bash
$ python manage.py runserver
```

## Testes

Você pode rodar os testes unitários:

```bash
$ python manage.py test
```

Licença: GPL
