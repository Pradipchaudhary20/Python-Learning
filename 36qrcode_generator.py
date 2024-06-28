#Qr code Generator
import qrcode
img = qrcode.make('PradipChaudhary')
type(img)  # qrcode.image.pil.PilImage
img.save("Pradip.png")

### WiFI LinK
wifi_type  = "WPA"
wifi_ssid = "Popat5G"
wifi_password = "9745524762"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make('Wifi')
type(img)  # qrcode.image.pil.PilImage
img.save("Popat5g.png")