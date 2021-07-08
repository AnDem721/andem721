import psutil


def print_pids():
    pids_list = psutil.pids()
    for x in pids_list:
        print(x)

print_pids()
