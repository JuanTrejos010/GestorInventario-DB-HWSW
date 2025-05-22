#Librerías
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
import os
import uvicorn
from fastapi.templating import Jinja2Templates

#importar otros módulos
from database import crear_db, get_session
from computador import Computador

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory=".")
app= FastAPI()

#Funciones para llamar los recursos para la página web
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("Inicio.html", {"request": request})
@app.get("/InventarioSalones.html")
def inventario(request: Request):
    return templates.TemplateResponse("InventarioSalones.html", {"request": request})
@app.get("/InventarioSNuevo.html")
def inventarioN(request: Request):
    return templates.TemplateResponse("InventarioSNuevo.html", {"request": request})
@app.get("/PrestamosProf.html")
def PrestamosProf(request: Request):
    return templates.TemplateResponse("PrestamosProf.html", {"request": request})
@app.get("/NoFuncionales.html")
def NoFuncionales(request: Request):
    return templates.TemplateResponse("NoFuncionales.html", {"request": request})
@app.get("/CSS/Estilo.css")
async def get_css():
    return FileResponse("CSS/Estilo.css")
    
#Funciones de bases de datos
@app.get("/inventarioN", response_class=HTMLResponse)
def mostrar_Inventario(request: Request):
    return templates.TemplateResponse("InventarioSNuevo.html", {"request": request})
@app.post("/inventarioN", response_class=HTMLResponse)
def subir_Inventario(request: Request):
    pass
    
#Funciones para ejecutar el sistema


#ejecución del servidor
if __name__ == "__main__":
    crear_db()
    get_session()
    uvicorn.run(app, host="0.0.0.0", port=8005)
