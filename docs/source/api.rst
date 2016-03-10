API
===

.. todo::

   Usar a opção de autohttp.flask para atualizar automaticamente essa seção


Nessa seção vamos definir toda a documentação da API do projeto.

Autenticação
------------

Em breve

Documentos
----------

Nesse recurso, é aonde fica disponibilizado e persistido os documentos do projeto. Temos as seguintes URIs:

.. http:get:: /api/v1/(string:bucket)/documentos/

   Lista os documentos de um determinado sistema a partir do seu `bucket`.

   **Exemplo de requisição**:

   .. sourcecode:: http

      GET /api/v1/procult/documentos/ HTTP/1.1
      Authorization: Token 1af538baa9045a84c0e889f672baf83ff24
      Host: octofiles.cultura.df.gov.br

   :param bucket: Nome do bucket do sistema.
   :reqheader Authorization: Token para autenticação

   **Exemplo de resposta**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
          {
              "document_url": "http://octofiles.cultura.df.gov.br/api/v1/procult/propostas/alsd01lkasd9123jalsd123.pdf",
              "self_url": "http://octofiles.cultura.df.gov.br/api/v1/procult/ask12312309aslk1230",
              "metadata": {
                "name": "Fotos do Show",
                "type": "pdf",
                "size": 1200000
              },
              "owner_uid": "asdk1239asdlk12309as",
              "mode": "private"
          }
      ]

   :resheader Content-Type: Formato JSON
   :status 200: Requisição aceita com sucesso
   :status 400: Problema na requisição enviada
   :status 500: Erro na consulta dos documentos


.. http:post:: /api/v1/(string:bucket)/documentos/

   Envia um novo documento para armazenamento, a partir do seu `bucket`.

   :param bucket: Nome do bucket do sistema
   :form name: Nome do Arquivo
   :form path: Caminho do arquivo a ser salvo
   :form file: Binário do arquivo para upload
   :form mode: Modo de visualização: `public` ou `private`
   :form owner: Se o modo de visualização for `private`, o identificador único do dono do arquivo
   :reqheader Authorization: Token para autenticação
   :resheader Content-Type: Formato JSON
   :resheader Location: URI do arquivo recém criado
   :status 201: Documento criado com sucesso
   :status 400: Erro na montagem da requisição para upload do arquivo
   :status 500: Erro durante o upload do arquivo


.. http:get:: /api/v1/(string:bucket)/(string:uid)

   Retorna informações do documento pesquisado a partir do seu `bucket` e o `uid` do arquivo.

   **Exemplo de requisição**:

   .. sourcecode:: http

      GET /api/v1/procult/ask12312309aslk1230 HTTP/1.1
      Authorization: Token 1af538baa9045a84c0e889f672baf83ff24
      Host: octofiles.cultura.df.gov.br

   :param bucket: Nome do bucket do sistema.
   :param uid: Identificador único (UID) do arquivo salvo
   :reqheader Authorization: Token para autenticação

   **Exemplo de resposta**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
          "document_url": "http://octofiles.cultura.df.gov.br/api/v1/procult/propostas/alsd01lkasd9123jalsd123.pdf",
          "self_url": "http://octofiles.cultura.df.gov.br/api/v1/procult/ask12312309aslk1230",
          "metadata": {
            "name": "Fotos do Show",
            "type": "pdf",
            "size": 1200000
          },
          "owner_uid": "asdk1239asdlk12309as",
          "mode": "private"
      }

   :resheader Content-Type: Formato JSON
   :status 200: Requisição aceita com sucesso
   :status 400: Problema na requisição enviada
   :status 500: Erro na consulta do documento


.. http:put:: /api/v1/(string:bucket)/(string:uid)

   Atualiza as informações do documento selecionado a partir do seu `bucket` e o `uid` do arquivo.

   :param bucket: Nome do bucket do sistema
   :param uid: Identificador único (UID) do arquivo salvo
   :form name: Nome do Arquivo
   :form mode: Modo de visualização: `public` ou `private`
   :form owner: Se o modo de visualização for `private`, o identificador único do dono do arquivo
   :reqheader Authorization: Token para autenticação
   :resheader Content-Type: Formato JSON
   :resheader Location: URI do arquivo recém criado
   :status 200: Documento atualizado com sucesso
   :status 400: Erro na montagem da requisição para atualização do arquivo
   :status 500: Erro durante atualização do arquivo


.. http:delete:: /api/v1/(string:bucket)/(string:uid)

   Remove o documento selecionado a partir do seu `bucket` e o `uid` do arquivo.

   :param bucket: Nome do bucket do sistema
   :param uid: Identificador único (UID) do arquivo salvo
   :reqheader Authorization: Token para autenticação
   :status 204: Documento excluido com sucesso
   :status 400: Erro na montagem da requisição para remoção do arquivo
   :status 500: Erro durante remoção do arquivo
