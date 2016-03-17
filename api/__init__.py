# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from api.models import db
from config import config

bootstrap = Bootstrap()


def create_api(config_name=None):
    """
    Criando a instancia da aplicacao e registrando as extensoes
    a serem usadas, como os blueprints do projeto.
    """
    api = Flask(__name__)
    api.config.from_object(config[config_name])

    db.init_app(api)
    bootstrap.init_app(api)

    from api.admin.auth import admin_auth as admin_auth_blueprint
    api.register_blueprint(admin_auth_blueprint, url_prefix='/admin/auth')

    # from api.v1.oauth import oauth as oauth_blueprint
    # api.register_blueprint(oauth_blueprint,
    #                        url_prefix='/api/v1/auth')

    # from api.v1.documents import documents as documents_blueprint
    # api.register_blueprint(documents_blueprint,
    #                        url_prefix='/api/v1/documents')

    return api
