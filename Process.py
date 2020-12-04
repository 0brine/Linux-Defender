import Protocols


class Process:
    def __init__(self, host, port, protocol, interval=300):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.interval = interval
        self.results = []
        self.countdown = 0

    @property
    def status(self):
        if len(self.results) < 1:
            return "-"
        elif len(self.results) < 2:
            return "g" if self.results[-1] else "r"
        else:
            return "g" if self.results[-1] else "o" if self.results[-2] else "r"

    def action(self):
        worked = Protocols.pscan(self.host, self.port, self.protocol)
        self.results.append(worked)
