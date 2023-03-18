from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():    
        
    return {'Mensagem':'Ola, você esta na home'}



@app.get("/cadastro")
def cadatro():
    return {'Mensagem':'Cadastro'}



@app.get("/login")
def login():
    return {'Mensagem':'Login'}





