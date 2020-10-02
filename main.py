import socket

target = ""
port = 0


def pscan(t, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Target', t, '\nPort', p, end=' ')
    try:
        s.connect((t, p))
        print('is open\n')
    except:
        print('is closed\n')


pscan("10.24.17.6", 25)     #smtp
pscan("www", 80)            #http
pscan("10.24.17.6", 443)    #https
