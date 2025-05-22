#Librerías
from sqlmodel import Field, SQLModel, create_engine
from datetime import date

#Clase para añadir Inventario
class Inventario(SQLModel, table=true):
  id: int= Field(default=None, index=True, primary_key=True)
  Nombre:str
  Descripcion:str
  Salon:str
  LugCompra:str
  FechaCompra:date
  Estado:string
  
  
  
