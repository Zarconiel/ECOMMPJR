from fastapi import APIRouter, HTTPException, status
from uuid import uuid4
from datetime import datetime
import re
from typing import Dict

from models.user_models import UserCreate, User, UserUpdate, UserEditable
from database.json_db import db, save_db

router = APIRouter(prefix="/users", tags=["Usuários"])

# ================================
# Funções auxiliares
# ================================
def email_exists(email: str) -> bool:
    for user in db.values():
        if user.get("email", "").lower() == email.lower():
            return True
    return False

def cnpj_exists(cnpj: str) -> bool:
    cnpj_norm = re.sub(r'\D', '', cnpj)
    for user in db.values():
        if re.sub(r'\D', '', user.get("cnpj", "")) == cnpj_norm:
            return True
    return False

# ================================
# Rotas
# ================================

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
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

@router.get("/", response_model=list[User])
def list_users():
    return list(db.values())

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return db[user_id]

@router.get("/{user_id}/edit", response_model=UserEditable)
def get_user_editable(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    user = db[user_id]
    return {
        "nome": user.get("nome"),
        "cidade": user.get("cidade"),
        "telefone": user.get("telefone"),
        "ramo": user.get("ramo")
    }

@router.put("/{user_id}", response_model=User)
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
        )

    user = db[user_id]
    user.update(incoming)
    db[user_id] = user
    save_db(db)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    del db[user_id]
    save_db(db)
    return None
