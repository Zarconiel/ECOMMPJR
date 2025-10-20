from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI(title="API ECOMPJR")

# Rota raiz
@app.get("/")
def root():
    return {"msg": "API com validação de CNPJ e E-mail únicos (aceita CNPJs falsos)"}

# Inclui as rotas de usuário
app.include_router(user_router)
