#Email Qr code generator
import qrcode
email_address = 'iampradip.chy@gmail.com'
subject = 'My First Email Using Python'
body = 'Hello, this is my first email using Python.'
email = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(email)
type(img)
img.save("email.png")
