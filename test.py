from subprocess import PIPE, Popen


def cmdline(args):
    process = Popen(
        args=args,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0].decode("utf-8", errors='ignore')
