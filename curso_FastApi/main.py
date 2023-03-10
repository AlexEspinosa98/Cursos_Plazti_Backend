from fastapi import FastAPI


# Tenemos variable que mantiene toda la aplicación en app
app = FastAPI()

#Creando PathOperations
#Obtenemos la decoración inicial
@app.get("/")
def home():
    return {"Hello ": "World"}
    pass