import socket
import re

protocols = {
    "ssh": ["SSH-2.*"],
    "smtp": ["220.*", "HELO test", "250.*", "quit"],
    "http": ["", "get", ".*400 Bad Request[.,\s]*"],
    "https": ["", "get"],
    "imap": ["\\* OK.*", "0011 LOGOUT", "a"],
    "imaps": ["", "test", "\\* BYE Fatal error: tls_start_servertls\\(\\) failed"],
    "pop3": ["\\+OK.*", "quit"],
}


def pscan(host, port, protocol):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Target', host, '\nPort', port, end=' ')
    # try:
    s.connect((host, port))
    print('is open')

    worked = runProtocol(s, protocol)
    if worked:
        print("Protocol " + protocol + " worked fine")
    # except:
    #    print('is closed\n-------- ERROR --------\n')


def runProtocol(s, protocolName):
    protocol = protocols[protocolName]
    worked = True

    for i in range(len(protocol)):
        string = protocol[i]
        if i % 2 == 0:
            if string == "":
                continue
            msg = s.recv(1024).decode("utf-8")
            print(msg)
            print(re.search("^" + string + "\\s*$", msg).string)
            worked = msg == re.search("^" + string + "\\s*$", msg).string
        else:
            s.send((string + "\r\n").encode())

        if not worked:
            print("Protocol " + protocolName + " did not work")
            break

    s.shutdown(0)
    s.close()

    return worked


#pscan("10.24.17.6", 25, "smtp")
# pscan("10.24.17.6", 22, "ssh")
pscan("10.24.17.6", 587, "smtp")
# pscan("www", 80, "http")
# pscan("10.24.17.6", 443, "https")
#pscan("10.24.17.6", 143, "imap")
#pscan("10.24.17.6", 993, "imaps")
# pscan("10.24.17.6", 110, "pop3")
