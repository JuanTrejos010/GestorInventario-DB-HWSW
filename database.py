#Llamando las librerías
from sqlmodel import SQLModel, create_engine, Session

#Condiciones de la conexión a la base de datos
user = "root"
password = "CSM24+DfH"
host = "localhost"
port = 3306
nombre_bd = "escolar"

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{port}"
enginetmp = create_engine(DATABASE_URL)
with engine_tmp.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}"))
    print(f"Base de datos '{nombre_bd}' verificada o creada.")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{nombre_bd}"
engine = create_engine(DATABASE_URL)



with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}"))
    print(f"Base de datos '{nombre_bd}' verificada o creada.")

def crear_db():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session