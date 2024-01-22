from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory=".") #especifico la carpeta donde tengo las plantillas (archivos html), 
# en este caso es la misma carpeta del main
@app.get('/formulario',response_class=HTMLResponse)
def read_form(request: Request):
    # Usas el objeto templates para renderizar la plantilla "form_template.html".
    # Pasas los detalles de la solicitud a la plantilla.
    return templates.TemplateResponse("form_template.html", {"request": request})

# Defines una ruta POST para "/submit_form". 
# Esta ruta manejará los datos del formulario cuando se envíen.
@app.post("/submit_formulario")
def submit_form(username: str = Form(...), password: str = Form(...)):
    # Los datos del formulario se reciben como parámetros de la función.
    # Usas la función Form de FastAPI para declararlos y recibirlos.
    # Luego, devuelves los datos del formulario como un diccionario.
    return {"username": username, "password": password}