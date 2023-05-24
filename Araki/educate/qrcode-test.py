import qrcode
img = qrcode.make("https://kujirahand.com/")
img.save("qrcode-test.png")