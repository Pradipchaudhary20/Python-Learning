#sms qr code
import qrcode
phone_number = "9867154085"
message = "Hello how are you ?"
sms = f"SMSTO:<phone_number>:<message>"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")