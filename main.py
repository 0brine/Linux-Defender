import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("What website to scan: ")


def pscan(port):
    try:
        s.connect((target, port))
        return True
    except:
        return False


x = 80
print('Port', x, end=' ')

if pscan(x):
    print('is open')
else:
    print('is closed')
