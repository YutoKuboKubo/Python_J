import os
import sys
import qrcode


args = sys.argv
url = args[1]
file_name = args[2]
# QRコードを作成
img = qrcode.make(url)
# パスを指定
path = os.path.join("..", "files", f"{file_name}.png")
# QRコードを保存
img.save(path)
