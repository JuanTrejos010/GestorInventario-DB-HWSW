from sqlmodel import Field, SQLModel, create_engine

class Inventario(SQLModel, table=true):
  id: Optional[int] = Field(default=None, index=True, primary_key=True)
  Nombre:str
  Descripcion:str
  Salon:str
  LugCompra:str
  
  
