mport segno

'''
important commands to execute binary file 
    1. chmod +x application.bin
    2. ./application.bin

base64 to binary convereter website
https://base64.guru/converter/decode/file

'''
global string 
string = ""
def reader(filename):
    string = ""
    with open(filename) as f:
        for x in range(48677):
            #we have to divide the total characters by the max char length of the qr code
                #we can use the structures append feature 
            
            char = f.read(1)
            
            if char:
                string = string + char
                if char == "=": 
                    print("shit cum poop stain", " ", x)
            else:
                return


r = reader('base64mc4k.txt')

print(string)

qrcode_seq = segno.make_sequence(string, version=40)


qrcode_seq.save('testQRCODES.svg', scale=10)
















