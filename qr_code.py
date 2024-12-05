import os
from qrcode import QRCode
from dotenv import load_dotenv

def generate_qr_code(data):
    qr = QRCode()
    qr.add_data(data)
    qr.make()
    img = qr.make_image(
        fill_color="white",
        back_color="black"
    )
    return img

if __name__ == "__main__":
    load_dotenv(override=True)
    BASE_URL = os.environ.get("BASE_URL")
    qr_code = generate_qr_code(
        f"{BASE_URL}/fantasia.html"
    )
    qr_code.show()