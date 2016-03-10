# -*- coding: utf-8 -*-

from flask import Flask
from api.models import db
from config import config


def create_api(config_name=None):
    """
    Criando a instancia da aplicacao e registrando as extensoes
    a serem usadas, como os blueprints do projeto.
    """
    api = Flask(__name__)
    api.config.from_object(config[config_name])

    db.init_app(api)

    # from api.v1.documents import documents as documents_blueprint
    # api.register_blueprint(documents_blueprint, url_prefix='/api/v1')

    return api
