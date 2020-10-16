import socket


def pscan(host, port, protocoll):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Target', host, '\nPort', port, end=' ')
    try:
        s.connect((host, port))
        print('is open')

        print(s.recv(1024));
    except:
        print('is closed\n-------- ERROR --------\n')


pscan("10.24.17.6", 22, "ssh")
pscan("10.24.17.6", 25, "smtp")
pscan("10.24.17.6", 587, "smtp")
pscan("www", 80, "http")
pscan("10.24.17.6", 443, "https")
pscan("10.24.17.6", 143, "imap")
pscan("10.24.17.6", 993, "imaps")
pscan("10.24.17.6", 110, "pop3")
pscan("10.24.17.6", 995, "pop3s")
