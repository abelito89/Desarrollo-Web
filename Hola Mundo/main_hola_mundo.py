from fastapi import FastAPI

perro = FastAPI()
@perro.get("/")
async def root():
    return {"message": "Hello World"}