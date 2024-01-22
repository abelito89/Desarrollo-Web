from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Form

app = FastAPI()
templates = Jinja2Templates(directory = './Templates')

@app.get('/formulario', response_class=HTMLResponse)
def leer_formulario(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/seleccionar_operacion')
def submit_form(request:Request,valor1:float=Form(...), valor2:float=Form(...), operacion:str=Form(...)):
   
    if operacion == 'sumar':
        resultado = valor1+valor2
    elif operacion == 'restar':
        resultado = valor1-valor2
    elif operacion == 'multiplicar':
        resultado = valor1*valor2
    elif operacion == 'dividir':
        if valor2 == 0:
            resultado = 'La división por cero no está permitida'
        else:
            resultado = valor1/valor2      

    return templates.TemplateResponse('operacion.html', {"request": request,'resultado':resultado}) 