#Llamando las librerías
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/escolar"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def crear_db:
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session