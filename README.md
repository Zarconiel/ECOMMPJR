# Desafio API ECOMPJR: Cadastro de Empresas
**Sobre o Projeto**
Este projeto consiste na construção de uma API RESTful para o gerenciamento (Cadastro, Leitura, Atualização e Deleção - CRUD) de informações de empresas.

A API permite registrar novas empresas, realizar consultas específicas por ID, atualizar dados cadastrais e remover registros, sendo ideal para sistemas que necessitam de um repositório centralizado de dados empresariais.

## ⚙️Funcionalidades
As principais funcionalidades da API são:

- Criação de novos cadastros de empresas.

- Leitura da lista completa de empresas ou de uma empresa específica por ID.

- Atualização das informações cadastrais (com restrições em campos críticos).

- Deleção de registros de empresas.

- Validação de unicidade de E-mail e CNPJ no momento do cadastro.

## 🛠️Tecnologias Utilizadas
O projeto foi desenvolvido com as seguintes ferramentas e bibliotecas:

- Linguagem: Python 3.13.2

- Framework Web: FastAPI

- Validação de Dados: Pydantic

- Manipulação de Dados: JSON

- Data e Hora: datetime

- Servidor ASGI: Uvicorn

## 🧭Endpoints da API
A documentação interativa (Swagger UI) está disponível em http://127.0.0.1:8000/docs.

## Rsumo das rotas
| Operação  | Método HTTP || Rota (Endpoint)|Finalidade |Status de Sucesso|
| CREATE    | POST        || /users/cadastro| Registra uma nova empresa.|201 Created|
| READ (Todos)| GET       || /users/ |Retorna a lista completa de empresas.|200 OK|
| READ        | GET || /users/{user_id} | Busca uma empresa pelo ID.|200 OK|
(Específico)
| UPDATE| PUT             || /{user_id}/edit | Atualiza dados cadastrais da empresa (exceto e-mail/CNPJ/criação).|200 OK|
| DELETE | DELETE         || /{user_id}/del | Remove o registro de uma empresa.|204 No Content|

## Detalhe dos Endpoints

|Rota|	Tipo|	Parâmetros / Body (Payload)|	Descrição da Funcionalidade|	Observações Importantes|
|/users/|	GET	|Nenhum	|Lista todas as empresas cadastradas no sistema.|	Retorna uma lista de objetos User.|
|/users/{user_id}|	GET	|user_id (path)|	Realiza a busca de uma empresa específica utilizando seu ID único.	|Retorna 404 se o ID não for encontrado.|
|/users/cadastro|	POST|	payload: UserCreate (body)|	Utilizada para o cadastro de novas empresas.	Retorna 400 se o E-mail ou CNPJ já estiverem cadastrados.|
|/{user_id}/edit	|PUT	|user_id (path), payload: UserUpdate (body)|	Atualiza informações da empresa.	Não é permitido alterar os campos email, cnpj e created_at. Retorna 400 se tentar.|
|/{user_id}/del	|DELETE	|user_id (path)|	Deleta o registro da empresa.|	Retorna 404 se o ID não for encontrado|





## ⚠️ Problemas e Sugestões de Melhoria
Esta aplicação é funcional, mas atualmente armazena os dados em memória (in-memory storage), resultando na perda de todos os dados registrados após o desligamento da aplicação.

**Sugestão de Melhoria Principal:**
**Persistência de Dados:** Implementar um módulo de banco de dados (como SQLite, PostgreSQL ou MongoDB) para garantir que todos os dados registrados e atualizados sejam mantidos mesmo após o reinício da aplicação.

## 🧑‍💻 Autor
Desenvolvido por: **Carlos Daniel**