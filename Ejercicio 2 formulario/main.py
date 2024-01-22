from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="./Templates")
precios = {
    "Dados de queso": 5.00,
    "Coctel de frutas": 4.50,
    "Crema de queso": 5.50,
    "Cerdo a la plancha": 10.00,
    "Cerdo al carbón": 11.00,
    "Espaguettis": 8.00,
    "Copa lolita": 3.50,
    "Brownie": 4.00,
    "Tartaleta": 4.50
}

@app.get('/formulario', response_class=HTMLResponse)
def read_form(peticion:Request):
    return templates.TemplateResponse('index.html',{"request":peticion, 'precios':precios})

@app.post('/submit_menu')
def submit_menu(peticion:Request, entrante:str=Form(...), plato_principal:str=Form(...), postre:str=Form(...)):
    precio_total = precios[entrante] + precios[plato_principal] + precios[postre]
    return templates.TemplateResponse('menu.html',{'request':peticion,'precio_total':precio_total,'entrante_elegido':entrante, 'plato_principal':plato_principal, 'postre_elegido':postre})