from database import Database
from qr_generator import QRGenerator

class Computador:
    def _init_(self):
        self.db = Database()
        self.qr_gen = QRGenerator()

    def agregar_computador(self, codigo_inventario, marca, modelo, procesador, ram_gb, almacenamiento_gb, tipo_almacenamiento, fecha_compra, estado):
        qr_path = self.qr_gen.generar_qr(f"Inventario: {codigo_inventario}", codigo_inventario)
        
        sql = """
        INSERT INTO Computadores (codigo_inventario, marca, modelo, procesador, ram_gb, almacenamiento_gb, tipo_almacenamiento, fecha_compra, estado, qr_code_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (codigo_inventario, marca, modelo, procesador, ram_gb, almacenamiento_gb, tipo_almacenamiento, fecha_compra, estado, qr_path)
        
        self.db.cursor.execute(sql, valores)
        self.db.commit()
        print(f"Computador '{codigo_inventario}' agregado exitosamente con QR en {qr_path}")

    def cerrar_conexion(self):
        self.db.close()
