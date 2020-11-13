import socket
import re

protocols = {
    "ssh": ["SSH-2.*"],
    "smtp": ["220.*", "HELO test", "250.*", "quit"],
    "http": ["", "get", ".*400 Bad Request.*"],
    "https": ["", "get"],
    "imap": ["\\* OK.*", "0011 LOGOUT"],
    "imaps": ["", "test", "\\* BYE Fatal error: tls_start_servertls\\(\\) failed"],
    "pop3": ["\\+OK.*", "quit"],
}


def pscan(host, port, protocol):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Target', host, '\nPort', port, end=' ')
    try:
        s.connect((host, port))
    except:
        print("Port " + port + " for protocol " + protocol + " is closed")

    worked = runProtocol(s, protocol)
    if worked:
        print("Protocol " + protocol + " worked fine")
    else:
        print("Protocol " + protocol + " did not work")


def runProtocol(s, protocolName):
    protocol = protocols[protocolName]
    worked = True

    for i in range(len(protocol)):
        string = protocol[i]
        if i % 2 == 0:
            if string == "":
                continue
            msg = s.recv(1024).decode("utf-8")
            worked = msg == re.search("^" + string + "\\s*$", msg, flags=re.DOTALL).string
        else:
            s.send((string + "\r\n").encode())

        if not worked:
            break

    s.shutdown(0)
    s.close()

    return worked
