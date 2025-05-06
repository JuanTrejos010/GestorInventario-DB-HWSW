#Para hacer: Importar FastAPI
from computador import Computador

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
