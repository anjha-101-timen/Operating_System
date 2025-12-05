import os
import subprocess

def task2_execute_commands(commands):
    for cmd in commands:
        pid = os.fork()

        if pid == 0:
            # Child executes Linux command
            print(f"\nExecuting command in child {os.getpid()}: {cmd}")
            subprocess.run(cmd, shell=True)
            os._exit(0)
        else:
            os.wait()
