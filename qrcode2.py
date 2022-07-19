from ensurepip import version
import qrcode


qr = qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4,)
qr.add_data("https://www.amazon.in/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("playlist.png")