# -*- coding: utf-8 -*-

import os
from flask import Flask
from api.models import db


def create_app(config=None):
    """
    Criando a instancia da aplicacao e registrando as extensoes
    a serem usadas, como os blueprints do projeto.
    """
    app = Flask(__name__)
    app.config.from_object(config or os.getenv('FLASK_CONFIG') or 'default')

    db.init_app(app)

    from api.v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
