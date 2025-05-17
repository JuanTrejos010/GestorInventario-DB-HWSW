#Librerías
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse,  FileResponse
import os
import uvicorn
from fastapi.templating import Jinja2Templates

#importar otros módulos
from computador import Computador

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory=".")
URL_DATABASE ="mysql+pymysql://root:@localhost:3306/escolar"
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
@app.get("/CSS/Estilo.css")
async def get_css():
    return FileResponse("CSS/Estilo.css")
    
    
def main():
    comp = Computador()

    # Crear las tablas si no existen
    comp.db.crear_tablas()

    # Agregar un computador de ejemplo
    comp.agregar_computador(
        codigo_inventario="PC001",
        marca="Dell",
        modelo="Latitude 5400",
        procesador="Intel Core i7",
        ram_gb=16,
        almacenamiento_gb=512,
        tipo_almacenamiento="SSD",
        fecha_compra="2023-06-10",
        estado="Activo"
    )

    comp.cerrar_conexion()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
