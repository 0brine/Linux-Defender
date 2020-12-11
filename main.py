import time
from Process import Process
processes = []


def tick():
    checks = 0
    for i, p in enumerate(processes):
        p.countdown -= 1

        if p.countdown <= 0:
            p.countdown = p.interval
            p.action()
            checks += 1

    return checks


def start():
    file = open("config.txt", "r")
    lines = file.readlines()

    for line in lines:
        params = line.replace(" ", "").replace("\n", "").split(",")

        processes.append(Process(params[0], int(params[1]), params[2], int(params[3]), params[4:]))

    changes = 0
    while True:
        changes += tick()
        if changes > 0:
            log_processes()

        time.sleep(1)


def log_processes():
    status_file = open("status.txt", "w")
    for p in processes:
        status_file.write(",".join([p.status, p.host, str(p.port), p.protocol]) + "\n")
    status_file.close()


start()
