import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

target = '10.24.17.6'
port = 25


def pscan(port):
    try:
        s.connect((target, port))
        return True
    except:
        return False


print('Port', port, end=' ')

if pscan(port):
    print('is open')
else:
    print('is closed')

result = s.recv(4096)

while len(result) > 0:
    print(result)
    result = s.recv(1024)
