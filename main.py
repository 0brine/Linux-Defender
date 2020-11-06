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


file = open("config.txt","r")
lines = file.readlines()

print(lines[0].split(","))
for line in lines:
    line = line.replace(" ", "")
    pscan(line.split(",")[0], int(line.split(",")[1]), line.split(",")[2])
    print(line)


#pscan("10.24.17.6", 25, "smtp")
#pscan("10.24.17.6", 22, "ssh")
#pscan("10.24.17.6", 587, "smtp")
#pscan("10.24.17.6", 443, "https")
#pscan("10.24.17.6", 993, "imaps")
#pscan("10.24.17.6", 110, "pop3")
#pscan("www", 80, "http")
#pscan("10.24.17.6", 143, "imap")

