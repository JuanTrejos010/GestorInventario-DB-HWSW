from sqlmodel import Field, SQLModel, create_engine

class Inventario(SQLModel, table=true):
  id: Optional[int] = Field(default=None, primary_key=True)
  Nombre:str
  
