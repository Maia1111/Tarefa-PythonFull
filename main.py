from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class Tarefas(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]


lista = []

@app.post('/inserir')
def inserir(tarefa:Tarefas):
    try:
      lista.append(tarefa)
      return {'stratus': 'sucesso!'}
    except:
       return {'status':'erro'}
    

@app.get('/listarTarefas')
def listar(opcao: int = 0):
   if opcao == 0:
      return lista
   if opcao == 1:
      return list(filter(lambda x: x.realizada == False, lista))
   if opcao == 2:
      return list(filter(lambda x: x.realizada == True, lista))
   

@app.get('/listarUnico/{id}')
def listarId(id: int):
   try:
      return lista[id]
   except:
      return {'status': 'erro'}
   
   
@app.post('/alteraStatus')
def alteraStatus(id: int):
   try:
      lista[id].realizada = not lista[id].realizada
      return {'status':'sucesso'}

   except:
      return {'status': 'erro'}
   
  
@app.post('/excluir')
def excluir(id: int):
   try:
    del lista[id]
    return {'status': 'sucesso!'}
   except:
      return {'status': 'erro'}