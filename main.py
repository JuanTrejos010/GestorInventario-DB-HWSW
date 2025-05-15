#Librerías
from fastapi import FastAPI, HTTPException
from computador import Computador
import os

URL_DATABASE ="mysql+pymysql://root:@localhost:3306/escolar"
app= FastAPI()

@app.get("/")
async def root():
    return {"Hola: Hola"}


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

if _name_ == "_main_":
    main()
