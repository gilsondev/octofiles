Funcionalidades
===============

O projeto Octofiles, como definido na introdução, ele oferece um serviço de armazenamento de documentos dos entes artísticos, como também alguns metadados de cada sistema, na necessidade de futuras consultas. Assim foi pensado nas seguintes funcionalidades.


Administradores
---------------

Aqui os administradores do sistema, terão a opção de manter os seus dados e de outros. Além disso ele terá o papel importante no gerenciamento dos sistemas autorizados a usar o serviço.

Gerenciamento de Sistemas
-------------------------

Sendo um Administrador, o usuário pode cadastrar os sistemas que vão ter acesso ao serviço do Octofiles. Nesse cadastro será gerado um `APP_ID` e um `SECRET_KEY`, em que o sistema consumidor precisará enviar a este, para gerar um token de autenticação e assim ser autorizado para enviar arquivos para upload como consulta e download. Além disso, o usuário poderá revogar o acesse de quem precisar.
