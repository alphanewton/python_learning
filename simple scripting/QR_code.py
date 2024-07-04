# Complex version with black and gold
# import qrcode
# from PIL import Image
#
# data = input("Enter data/web link:")
#
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
# qr.add_data(data)
# qr.make(fit=True)
#
# img = qr.make_image(fill_color = "gold", back_color = "black")
# img.save("QR_code.png")

# A simpler version of the code
import qrcode as qr
data = input("Enter data/web link:")
img = qr.make(data)
img.save("QRcode.png")