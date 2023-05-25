import qrcode
import sys

pas = sys.argv[1]

img = qrcode.make(pas)

img.save("/home/matcha-23training/files/aim.png")


