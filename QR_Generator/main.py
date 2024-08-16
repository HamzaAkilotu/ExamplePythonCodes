import pyqrcode

url = input("Enter URL to generate QR code: ")
qr_code = pyqrcode.create(url)
qr_code.svg("Example_QR_Code.svg", scale=3)