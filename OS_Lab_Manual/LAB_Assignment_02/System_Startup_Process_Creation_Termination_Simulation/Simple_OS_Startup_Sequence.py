# This program simulates a simple OS startup sequence. It creates processes, runs them, and logs their status to a file.
# Import required libraries
import multiprocessing
import time
import logging

# ---------------------------------------------------------
# Setup the Logger
# ---------------------------------------------------------
# Logging to file 'process_log.txt' with timestamp, process name and custom message
logging.basicConfig(filename='process_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(processName)s - %(message)s')

# ---------------------------------------------------------
# Dummy function that simulates a system process
# ---------------------------------------------------------
def system_process(task_name):
    logging.info(f"{task_name} started")   # Log process start
    time.sleep(2)                          # Simulate work
    logging.info(f"{task_name} ended")     # Log process end

# ---------------------------------------------------------
# Main Program: System Startup and Shutdown Simulation
# ---------------------------------------------------------
if __name__ == '__main__':
    print("System Starting...")

    # Create processes that simulate system services
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
    p3 = multiprocessing.Process(target=system_process, args=('Process-3',))

    # Start processes
    p1.start()
    p2.start()
    p3.start()

    # Wait until all processes finish execution
    p1.join()
    p2.join()
    p3.join()

    print("System Shutdown.")
