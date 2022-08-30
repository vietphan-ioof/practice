import sys, os
try:
    from pyzbar.pyzbar import decode, ZBarSymbol
except:
    cmd = ('py -m pip install "pyzbar"')
    os.system(cmd)
    from pyzbar.pyzbar import decode, ZBarSymbol

try:
    from PIL import Image
except:
    cmd = ('py -m pip install "Pillow"')
    os.system(cmd)
    from PIL import Image

decoded = decode(Image.open("bruhmoment6.jpg"), symbols=[ZBarSymbol.QRCODE])
qr_dic = {}
count = 0

for qr in decoded:
    print("QR")
    print(qr[1][0])
    x = qr[2][0] # The Left position of the QR code
    qr_dic[x] = qr[0] # The Data stored in the QR code


for qr in sorted(qr_dic.keys()):
    print(qr_dic[qr])
    count+=1

print(count)
