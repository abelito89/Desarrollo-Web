from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory = './Templates')

@app.get('/formulario', response_class=HTMLResponse)
def read_form(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/submit_formulario')
def submit_form(name: str=Form(...), edad:int=Form(...), correo:str=Form(...)):
    return {'name':name, 'edad': edad,'correo':correo}