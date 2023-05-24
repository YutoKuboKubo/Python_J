import qrcode
import os 

import sys
args = sys.argv

url = args[1]
file_name = args[2]

img = qrcode.make(url)
path = os.path.join("..", "..", "files",file_name)
img.save(path)