import pyqrcode
import os, shutil

title = input("Give Your QR Code a title! =>")
text = input("What Would You Like the QR Code to Say? =>")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.svg(file_name_png, scale=10)

os.mkdir(fr"C:\Users\Md. Alhad Kabir\Desktop\{title}")

shutil.move(file_name_png, fr"C:\Users\Md. Alhad Kabir\Desktop\{title}")
shutil.move(file_name_svg, fr"C:\Users\Md. Alhad Kabir\Desktop\{title}")

