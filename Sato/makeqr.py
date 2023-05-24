import qrcode

img = qrcode.make("http://kujirahand.com/")

img.save("/home/matcha-23training/files/qrcode-test.png")