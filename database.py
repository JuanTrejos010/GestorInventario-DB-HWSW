#Llamando las librerías
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text 

#Condiciones de la conexión a la base de datos
user = "root"
password = "CSM24+DfH"
host = "localhost"
port = 3306
#cambiar el port a 3307 al subirlo al Windows Server virtualizado
nombre_bd = "escolar"

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}"
engine_tmp = create_engine(DATABASE_URL)
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