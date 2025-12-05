# Task 1: Process Creation Using fork()

import os
import time

def task1_create_processes(n):
    children = []

    for i in range(n):
        pid = os.fork()

        if pid == 0:
            # Child process
            print(f"[Child] PID: {os.getpid()}, PPID: {os.getppid()}, Message: Child {i} created")
            os._exit(0)
        else:
            # Parent process
            children.append(pid)

    # wait for all children
    for child in children:
        os.wait()
