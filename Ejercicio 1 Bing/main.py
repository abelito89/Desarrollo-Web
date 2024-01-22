from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def mensaje():
    return "¡Hola, FastAPI!"

@app.get('/cubo/{numero}')
def cubo(numero:int):
    return str(numero**3)