from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from uuid import UUID
import re
from datetime import datetime

class UserCreate(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    cnpj: str = Field(..., description="CNPJ (será normalizado, aceita 'falso')")
    cidade: str
    telefone: str
    ramo: str

    @validator("cnpj")
    def normalizar_cnpj(cls, value: str) -> str:
        """Remove caracteres não numéricos do CNPJ."""
        return re.sub(r'\D', '', value)

class User(UserCreate):
    id: UUID
    created_at: datetime

class UserUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    cnpj: Optional[str]
    cidade: Optional[str]
    telefone: Optional[str]
    ramo: Optional[str]

class UserEditable(BaseModel):
    nome: str
    cidade: str
    telefone: str
    ramo: str
