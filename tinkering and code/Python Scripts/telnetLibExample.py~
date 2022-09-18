import telnetlib 
import json



HOST = "socket.cryptohack.org"
PORT = 11112



tn = telnetlib.Telnet(HOST, PORT)


def readLine():
    return tn.read_until(b"\n")

def json_recv():
    line = readLine()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readLine())
print(readLine())
print(readLine())
print(readLine())


request = {
        "buy": "flag"
        }

json_send(request)

response = json_recv()
print(response)








