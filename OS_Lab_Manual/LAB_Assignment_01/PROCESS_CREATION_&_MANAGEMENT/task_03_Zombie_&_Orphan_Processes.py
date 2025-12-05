def create_zombie():
    pid = os.fork()

    if pid == 0:
        print(f"[Child {os.getpid()}] Becoming zombie...")
        os._exit(0)
    else:
        print(f"[Parent {os.getpid()}] Not waiting → Zombie created")
        time.sleep(10)  # child becomes zombie

def create_orphan():
    pid = os.fork()

    if pid == 0:
        time.sleep(3)
        print(f"[Child {os.getpid()}] Parent died → Now adopted by init (PPID: {os.getppid()})")
        os._exit(0)
    else:
        print(f"[Parent {os.getpid()}] Exiting early → Child becomes orphan")
        os._exit(0)
