"""
 Ejercicio: Crea una API con FastAPI que tenga las siguientes rutas:

/suma/{num1}/{num2}: Esta ruta debe tomar dos números como parámetros y devolver la suma de ambos.

/resta/{num1}/{num2}: Esta ruta debe tomar dos números como parámetros y devolver la resta del primero menos el segundo.

/multiplica/{num1}/{num2}: Esta ruta debe tomar dos números como parámetros y devolver la multiplicación de ambos.

/divide/{num1}/{num2}: Esta ruta debe tomar dos números como parámetros y devolver la división del primero entre el segundo. 
Asegúrate de manejar el caso en que el segundo número sea cero para evitar errores de división por cero.   

    """
from fastapi import FastAPI
app = FastAPI()
@app.get('/suma/{num1}/{num2}')
def suma(num1:int,num2:int):
    return {'Suma':num1+num2}

@app.get('/resta/{num1}/{num2}')
def resta(num1:int,num2:int):
    return {'resta': num1-num2}

@app.get('/divide/{num1}/{num2}')
def divide(num1:int,num2:int):
    if num2 != 0:
        cociente = num1/num2
        return {'cociente':cociente}
    else:
        return {'error':'La division por cero no se permite'} 
