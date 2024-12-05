import os
from qrcode import QRCode
from dotenv import load_dotenv

load_dotenv(override=True)
BASE_URL = os.environ.get("BASE_URL")


def gerar_qr_code(lado_camiseta: str):
    qr = QRCode()
    qr.add_data(f"{BASE_URL}/{lado_camiseta}.html")
    qr.make()
    img = qr.make_image(fill_color="white", back_color="black")
    return img


lado_camiseta = "frente"
qr_code = gerar_qr_code(lado_camiseta)
qr_code.show()
