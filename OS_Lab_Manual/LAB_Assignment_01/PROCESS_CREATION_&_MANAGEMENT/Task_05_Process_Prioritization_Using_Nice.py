def cpu_task():
    x = 0
    for i in range(50000000):
        x += i

def task5_priority_demo():
    for nice_value in [0, 5, 10]:
        pid = os.fork()

        if pid == 0:
            os.nice(nice_value)
            print(f"[Child {os.getpid()}] Running with nice={nice_value}")
            cpu_task()
            print(f"[Child {os.getpid()}] Completed with nice={nice_value}")
            os._exit(0)
        else:
            os.wait()
