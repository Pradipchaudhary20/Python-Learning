#Website Qrcode
import qrcode
img = qrcode.make('https://assignblog.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("Assignblog.png")

