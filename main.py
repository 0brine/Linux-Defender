import time
from Process import Process

processes = []


def tick():
    for p in processes:
        p.countdown -= 1

        if p.countdown <= 0:
            p.countdown = p.interval
            p.action()


def start():
    file = open("config.txt", "r")
    lines = file.readlines()

    for line in lines:
        params = line.replace(" ", "").replace("\n", "").split(",")

        processes.append(Process(params[0], int(params[1]), params[2], int(params[3])))

    while True:
        tick()
        time.sleep(1)



start()


#pscan("10.24.17.6", 25, "smtp")
#pscan("10.24.17.6", 22, "ssh")^^
#pscan("10.24.17.6", 587, "smtp")
#pscan("10.24.17.6", 443, "https")
#pscan("10.24.17.6", 993, "imaps")
#pscan("10.24.17.6", 110, "pop3")
#pscan("www", 80, "http")
#pscan("10.24.17.6", 143, "imap")
