
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str

lista = [Usuario(id=1, nome='Caio',senha='1234'), 
         Usuario(id=2, nome='Marcos', senha='2345'),
         Usuario(id=3, nome='João', senha='123456')]

@app.post('/usuario')
def main(usuario:Usuario):
    lista.append(usuario)
    return "Usuario cadastrado"

@app.get('/listar')
def main():
    return lista