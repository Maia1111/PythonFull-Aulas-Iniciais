from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

usuarios = [(1,'caio', 'minhasenha1'),(2,'João','minhasenha2')]

@app.post('/usuario')
def main(nome):
    
    for i in usuarios:
        if i[1] == nome:
            return i       

    return "Não existe esse usuário!"