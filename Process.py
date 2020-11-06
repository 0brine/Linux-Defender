import main


class Process:
    def __init__(self, host, port, protocol, interval):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.interval = interval
        self.countdown = interval

    def action(self):
        main.pscan(self.host, self.port, self.protocol)
