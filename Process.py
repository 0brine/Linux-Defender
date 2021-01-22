import Protocols


class Process:
    def __init__(self, host, port, protocol, interval=300, args=[], display=True):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.interval = interval
        self.results = []
        self.countdown = 0
        self.args = args
        self.display = display

    @property
    def status(self):
        if len(self.results) < 1:
            return "-"
        elif len(self.results) < 2:
            return "g" if self.results[-1] else "r"
        else:
            return "g" if self.results[-1] else "o" if self.results[-2] else "r"

    def action(self):
        worked = Protocols.pscan(self.host, self.port, self.protocol, self.interval, self.args)
        self.results.append(worked)
        print(",".join([self.status, self.host, str(self.port), self.protocol]))
