# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy

# Criando a instancia de SQLAlchemy
db = SQLAlchemy()

# Importando models para reconhecimento do Alembic
from api.models import * # NOQA
