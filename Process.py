import Protocols


class Process:
    def __init__(self, host, port, protocol, interval = 300):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.interval = interval
        self.countdown = 0

    def action(self):
        Protocols.pscan(self.host, self.port, self.protocol)

