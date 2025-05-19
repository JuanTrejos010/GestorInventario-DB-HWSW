from database import get_session
from qr_generator import QRGenerator
from sqlmodel import Session

class Computador:
    def __init__(self):
        self.qr_gen = QRGenerator()

    def agregar_computador(self, session: Session, codigo_inventario, marca, modelo, procesador, ram_gb, almacenamiento_gb, tipo_almacenamiento, fecha_compra, estado):
        qr_path = self.qr_gen.generar_qr(f"Inventario: {codigo_inventario}", codigo_inventario)

        # Aquí deberías usar un modelo SQLModel y hacer session.add(...)
        # Pero como estás usando SQL directo, podrías hacer:
        session.exec(
            """
            INSERT INTO Computadores (codigo_inventario, marca, modelo, procesador, ram_gb, almacenamiento_gb, tipo_almacenamiento, fecha_compra, estado, qr_code_path)
            VALUES (:codigo_inventario, :marca, :modelo, :procesador, :ram_gb, :almacenamiento_gb, :tipo_almacenamiento, :fecha_compra, :estado, :qr_code_path)
            """,
            {
                "codigo_inventario": codigo_inventario,
                "marca": marca,
                "modelo": modelo,
                "procesador": procesador,
                "ram_gb": ram_gb,
                "almacenamiento_gb": almacenamiento_gb,
                "tipo_almacenamiento": tipo_almacenamiento,
                "fecha_compra": fecha_compra,
                "estado": estado,
                "qr_code_path": qr_path
            }
        )
        session.commit()

    def cerrar_conexion(self):
        pass  # No se necesita si usas FastAPI con Depends(get_session)
