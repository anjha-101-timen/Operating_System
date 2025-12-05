def task4_read_proc(pid):
    print("\nReading /proc info...\n")

    # Read status
    with open(f"/proc/{pid}/status") as f:
        status_data = f.read()
    print(status_data)

    # Executable path
    exe_path = os.readlink(f"/proc/{pid}/exe")
    print("\nExecutable Path:", exe_path)

    # File descriptors
    fds = os.listdir(f"/proc/{pid}/fd")
    print("\nOpen File Descriptors:", fds)
