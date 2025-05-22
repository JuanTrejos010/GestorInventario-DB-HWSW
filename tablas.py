#Librerías
from sqlmodel import Field, SQLModel, create_engine
from datetime import date

#Para los atributos de las clases para las tablas, se debe usar CamelCase.

#Clase para añadir Inventario
class Inventario(SQLModel, table=true):
  id: int= Field(default=None, index=True, primary_key=True)
  Nombre:str
  Descripcion:str
  Salon:str
  LugCompra:str
  FechaCompra:date
  Estado:str
  
#Clase para añadir préstamos
class PrestamoP(SQLModel, table=true):
    id: int= Field(default=None, index=True, primary_key=True)
    Equipo:str
    Profesor:str
    LugarCompra:str
    FechaCompra:date
    FechaPrestamo:date
    Estado:str

'''
@app.post("/submit")
async def guardar_usuario(
    nombre: str = Form(...),
    fecha_nacimiento: str = Form(...)
):
    # Convertir string a objeto date
    fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
'''
  
  
  
