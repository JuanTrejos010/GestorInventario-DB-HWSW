#Llamando las librerías
from sqlmodel import SQLModel, create_engine, Session

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/escolar"
engine = create_engine(DATABASE_URL, echo=True)

def crear_db:
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session

class Database:
    def _init_(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",  # Cambia aquí tu contraseña
            database="colegio_computadores"
        )
        self.cursor = self.db.cursor()

    def crear_tablas(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS colegio_computadores")
        self.cursor.execute("USE colegio_computadores")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Computadores (
            id_computador INT PRIMARY KEY AUTO_INCREMENT,
            codigo_inventario VARCHAR(50) UNIQUE NOT NULL,
            marca VARCHAR(100),
            modelo VARCHAR(100),
            procesador VARCHAR(100),
            ram_gb INT,
            almacenamiento_gb INT,
            tipo_almacenamiento VARCHAR(50),
            fecha_compra DATE,
            estado VARCHAR(50),
            qr_code_path VARCHAR(255)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ubicaciones (
            id_ubicacion INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100),
            descripcion TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Asignaciones (
            id_asignacion INT PRIMARY KEY AUTO_INCREMENT,
            id_computador INT,
            id_ubicacion INT,
            fecha_asignacion DATE,
            observaciones TEXT,
            FOREIGN KEY (id_computador) REFERENCES Computadores(id_computador),
            FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Mantenimientos (
            id_mantenimiento INT PRIMARY KEY AUTO_INCREMENT,
            id_computador INT,
            fecha_mantenimiento DATE,
            tipo_mantenimiento VARCHAR(100),
            descripcion TEXT,
            costo_aproximado DECIMAL(10,2),
            FOREIGN KEY (id_computador) REFERENCES Computadores(id_computador)
        )
        """)
        print("Tablas creadas correctamente.")

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()
