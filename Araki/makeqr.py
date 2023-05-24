import qrcode
import os
import sys

args = sys.argv
qr_url = str(args[1])
filename = str(args[2])
img = qrcode.make(qr_url)
path = os.path.join("..","_pic",filename + ".png")
img.save(path)