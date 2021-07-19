import pyqrcode
qr = pyqrcode.create("test1")
qr.png("test1.png", scale=6)


from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('test1.png'))
print(data)