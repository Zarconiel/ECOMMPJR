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

## 🧭 Resumo das Rotas

| 💼 Operação | ⚙️ Método HTTP | 🛣️ Endpoint | 🧩 Finalidade | ✅ Status de Sucesso |
|:------------|:---------------:|:-------------|:--------------|:--------------------|
| 🆕 CREATE | **POST** | `/users/cadastro` | Registra uma nova empresa | 201 Created |
| 📜 READ (Todos) | **GET** | `/users/` | Retorna a lista completa de empresas | 200 OK |
| 🔍 READ (Por ID) | **GET** | `/users/{user_id}` | Busca uma empresa específica pelo ID | 200 OK |
| ✏️ UPDATE | **PUT** | `/{user_id}/edit` | Atualiza dados cadastrais (exceto e-mail/CNPJ/criação) | 200 OK |
| ❌ DELETE | **DELETE** | `/{user_id}/del` | Remove o registro de uma empresa | 204 No Content |
| 🔎 SEARCH | **GET** | `/users/search?ramo=Tech&cidade=Salvador` | Busca empresas por ramo e/ou cidade | 200 OK |


## 🧩 Detalhe dos Endpoints

| 🛣️ Rota | 🔢 Tipo | 📦 Parâmetros / Body | 🧭 Descrição da Funcionalidade | ⚠️ Observações Importantes |
|:---------|:--------:|:--------------------|:-------------------------------|:----------------------------|
| `/users/` | **GET** | Nenhum | Lista todas as empresas cadastradas no sistema | Retorna uma lista de objetos `User` |
| `/users/{user_id}` | **GET** | `user_id` *(path)* | Realiza a busca de uma empresa específica pelo ID | Retorna **404** se o ID não for encontrado |
| `/users/cadastro` | **POST** | `payload: UserCreate` *(body)* | Cadastra uma nova empresa | Retorna **400** se o E-mail ou CNPJ já existirem |
| `/{user_id}/edit` | **PUT** | `user_id` *(path)*, `payload: UserUpdate` *(body)* | Atualiza informações da empresa | Não é permitido alterar `email`, `cnpj` e `created_at` |
| `/{user_id}/del` | **DELETE** | `user_id` *(path)* | Deleta o registro da empresa | Retorna **404** se o ID não for encontrado |
| `/users/search` | **GET** | `ramo`, `cidade` *(query)* | Filtra empresas por ramo e/ou cidade | Retorna lista filtrada; ambos filtros são opcionais |





## ⚠️ Problemas e Sugestões de Melhoria
Esta aplicação é funcional, mas atualmente armazena os dados em memória (in-memory storage), resultando na perda de todos os dados registrados após o desligamento da aplicação.

**Sugestão de Melhoria Principal:**
**Persistência de Dados:** Implementar um módulo de banco de dados (como SQLite, PostgreSQL ou MongoDB) para garantir que todos os dados registrados e atualizados sejam mantidos mesmo após o reinício da aplicação.

## 🧑‍💻 Autor
Desenvolvido por: **Carlos Daniel**