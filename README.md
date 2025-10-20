# Desafio_api-ECOMPJR
 construçao de uma api para cadastro editavel de empresas.

 ## Funcionalidades 
 *cria, lê atualiza e deleta usuarios (crud)
 

 ## Tecnologias
 *Python 3.13.2
 *Fastapi
 *Pydantic
 *Json
 *datetime
 *uvicorn
 
 ## Aplicacação
 
 ### Rotas do tipo Get

 1-
 '''@router.get("/", response_model=list[User])
def list_users():
    return list(db.values())'''

Essa rota é feita para mostrar uma lista de empresas cadastradas 
*endpint: http://127.0.0.1:8000/users/ 

2-
'''@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return db[user_id] 
    '''

Essa rota faz busca especificas das empresas cadastradas atraves do seu ID 
*endpoint: http://127.0.0.1:8000/users/{id}

### Rotas do tipo Post 
1- 
'''@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate):
    if email_exists(payload.email):
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    if cnpj_exists(payload.cnpj):
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado.")

    new_id = uuid4()
    created_at = datetime.utcnow()

    user = User(id=new_id, created_at=created_at, **payload.dict())
    db[str(new_id)] = user.dict()
    save_db(db)
    return user
    '''

Essa rota é utilizada para o cadastro das empresas, ela verifica a existencia de Emails e CNPJ iguais se existir retornar um erro que esse campo ja existe em outra empresa
*endpoint: http://127.0.0.1:8000/users/cadastro 


### Rotas do tipo Put 
1- 
'''@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, payload: UserUpdate):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    incoming = payload.dict(exclude_unset=True)
    forbidden = {"email", "cnpj", "created_at"}
    intersect = forbidden.intersection(incoming.keys())
    if intersect:
        raise HTTPException(
            status_code=400,
            detail=f"Não é permitido alterar os campos: {', '.join(sorted(intersect))}."
        )'''

Essa rota é feita para atualizar as informaçoes das empresas exceto o Email, CNPJ, e a data de registro da empresa.
*endpoint: http://127.0.0.1:8000/{id}/edit
*endpoint: 
### Rotas do tipo Delete

1-
'''
@router.delete("/{user_id}/del", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    del db[user_id]
    save_db(db)
    return None
'''

Essa rota é utilizada para deletar as empresas cadastradas usando o seu ID
*endpoint: http://127.0.0.1:8000/{id}/del
