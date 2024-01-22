from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = './Templates')

candidatos_votos = {"Miguel Diaz-Canel Bermúdez":0, "Vladimir Putin":0, "Florentino Pérez":0}

@app.get('/formulario', response_class=HTMLResponse)
def leer_candidatos(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/votar')
def votar_candidatos(peticion:Request, candidato:str=Form(...)):
    for persona in candidatos_votos:
        if persona == candidato:
            candidatos_votos[persona]+=1
    return templates.TemplateResponse('votos.html',{'request':peticion, 'candidatos_votos':candidatos_votos})

@app.post('/resetear')
def resetear_votaciones(peticion:Request):
    for persona in candidatos_votos:
        candidatos_votos[persona] = 0
    return templates.TemplateResponse('index.html',{'request':peticion})