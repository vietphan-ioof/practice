import binascii 
import base64



hexVal = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"



temp = bytes.fromhex(hexVal)


print(temp.decode("utf-8"))


crypto{Base64EncodingisWebSafe}
