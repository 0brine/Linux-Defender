from test import cmdline
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
    # "ping": #TODO
}
special_protocols = {
    "ping": ["wsl ping $0 -c $1", ".*$1 packets transmitted, $1 received.*"],
}


def pscan(host, port, protocol, interval, args):

    if protocol in special_protocols:
        try:
            worked = test_special_protocols(host, port, protocol, interval, args)
        except:
            worked = False
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            worked = test_protocol(s, protocol)
        except:
            print("Port " + str(port) + " for protocol " + protocol + " is closed")
            worked = False

    return worked


def test_protocol(s, protocol_name):
    protocol = protocols[protocol_name]
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


def test_special_protocols(host, port, protocol_name, interval, args):
    protocol = special_protocols[protocol_name]

    command = protocol[0]\
        .replace("$0", host)\
        .replace("$1", str(port))\
        .replace("$2", protocol_name)\
        .replace("$3", str(interval))

    expected_output = protocol[1]\
        .replace("$0", host)\
        .replace("$1", str(port))\
        .replace("$2", protocol_name)\
        .replace("$3", str(interval))

    for i, a in enumerate(args):
        command = command.replace("$" + str(4 + i), str(a))
        expected_output = expected_output.replace("$" + str(4 + i), str(a))

    output = cmdline(command)

    return output == re.search("^" + expected_output + "\\s*$", output, flags=re.DOTALL).string
