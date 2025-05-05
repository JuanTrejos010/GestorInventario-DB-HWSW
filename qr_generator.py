import qrcode
import os

class QRGenerator:
    def _init_(self, qr_folder="qrs"):
        self.qr_folder = qr_folder
        if not os.path.exists(self.qr_folder):
            os.makedirs(self.qr_folder)

    def generar_qr(self, data, filename):
        path = os.path.join(self.qr_folder, f"{filename}.png")
        qr = qrcode.make(data)
        qr.save(path)
        return path
