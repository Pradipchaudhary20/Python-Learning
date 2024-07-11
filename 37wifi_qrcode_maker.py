import qrcode
#wifi Qrcode from userinput
wifi_type = input("Enter the wifi type (e.g WPA, WEP, or nopass: ").upper()
wifi_ssid = input('Enter your wifi name:  ')
wifi_password = input('Enter your wifi password:  ')
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("popat5g.png")




