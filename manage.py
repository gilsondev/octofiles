# -*- coding: utf-8 -*-

import os
from api import create_api, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

api = create_api(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(api)
migrate = Migrate(api, db)


def make_shell_context():
    """Insere as instancias da aplicacao e banco no contexto do shell"""
    return {
        'api': api,
        'db': db
    }
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    """Comando para execucao dos testes do projeto"""
    import pytest
    pytest.main("-s tests")

if __name__ == '__main__':
    manager.run()
