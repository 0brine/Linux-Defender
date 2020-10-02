import socket

target = ""
port = 0


def pscan(t, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Target', t, '\nPort', p, end=' ')
    try:
        s.connect((t, p))
        print('is open')
    except:
        print('is closed\n------------------------')


pscan("10.24.17.6", 22)     #ssh
pscan("10.24.17.6", 25)     #smtp
pscan("10.24.17.6", 587)    #smtp
pscan("www", 80)            #http
pscan("10.24.17.6", 443)    #https
pscan("10.24.17.6", 143)    #imap
pscan("10.24.17.6", 993)    #imaps
pscan("10.24.17.6", 110)    #pop3
pscan("10.24.17.6", 995)    #pop3s
