from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

df = pd.read_csv('txt_citas.txt', names=['Cita','Categoria'], sep=',')
app = FastAPI()
templates = Jinja2Templates('./Templates')

@app.get('/formulario_inicio', response_class=HTMLResponse)
def leer_formulario(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/enviar_categoria')
def enviar_categoria(peticion:Request, categoria:str=Form(...)):
    df_filtrado = df[df['Categoria'] == categoria]
    serie_aleatoria = df_filtrado.sample(n=1).iloc[0]
    cita_devuelta = serie_aleatoria['Cita']
    return templates.TemplateResponse('index.html',{'request':peticion, 'cita_devuelta':cita_devuelta})