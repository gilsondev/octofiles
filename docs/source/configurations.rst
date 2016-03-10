Configuração
============

Vamos orientar a configurar o projeto em um ambiente local, de duas formas: localmente para desenvolvimento e implantação. Lembrando que para todos os casos, precisa ter os seguintes requisitos mínimos:

 - Python 2.7 ou 3.2+
 - virtualenv
 - Git
 - PostgreSQL
 - Redis

Desenvolvimento
---------------

Acesse o repositório do projeto e efetue o checkout na sua máquina:

.. code-block:: bash

    $ git clone https://github.com/gilsondev/octofiles.git

Com o projeto no seu computador, vamos criar o ambiente virtual e instalar as dependências:

.. code-block:: bash

    $ cd octofiles
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

Instalado, vamos iniciar o servidor local:

.. code-block:: bash

    $ python manage.py runserver
