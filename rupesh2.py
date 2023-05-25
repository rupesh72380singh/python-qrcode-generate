import qrcode
from PIL import image
qr = qrcode.QRCode(version= 1 , error_correction=qrcode.constants.ERROR_CORRECT_H ,box_size=20,border=4)
qr.add_data("D:\photo mobile\IMG_20081231_213804.jpg")
qr.make(fit=True)
img= qr.make_image(fill_color="red" , back_color="blue")
image.save("suryam.png")