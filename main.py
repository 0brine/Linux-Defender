import time
from Process import Process
processes = []
last_config = ""
config_process = Process("", 0, "", 60, display=False)


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
    config_process.action = read_config
    config_process.action()

    changes = 0
    while True:
        changes += tick()
        if changes > 0:
            log_processes()

        time.sleep(1)


def log_processes():
    status_file = open("status.txt", "w")
    for p in processes:
        if not p.display:
            continue
        status_file.write(",".join([p.status, p.host, str(p.port), p.protocol]) + "\n")
    status_file.close()


def read_config():
    global last_config
    file = open("config.txt", "r")
    lines = file.readlines()
    if "".join(lines) == last_config:
        return

    last_config = "".join(lines)

    temp_processes = []
    for line in lines:
        params = line.replace(" ", "").replace("\n", "").split(",")

        temp_processes.append(Process(params[0], int(params[1]), params[2], int(params[3]), params[4:]))

    processes.clear()
    processes.append(config_process)
    processes.extend(temp_processes)

start()
