#Qr code Generator
import qrcode
img = qrcode.make('PradipChaudhary')
type(img)  # qrcode.image.pil.PilImage
img.save("Pradip.png")

