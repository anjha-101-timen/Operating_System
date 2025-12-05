# A. PRIORITY SCHEDULING (Non-Preemptive)
# Python Program

def priority_scheduling(processes):
    # processes = [(pid, arrival, burst, priority)]
    processes.sort(key=lambda x: (x[3], x[1]))  # Sort by priority, then arrival

    time = 0
    gantt = []
    waiting = []
    turnaround = []

    for p in processes:
        pid, arrival, burst, priority = p

        if time < arrival:
            time = arrival

        start = time
        end = time + burst
        gantt.append((pid, start, end))

        waiting.append(start - arrival)
        turnaround.append(end - arrival)

        time = end

    avg_wt = sum(waiting) / len(waiting)
    avg_tat = sum(turnaround) / len(turnaround)

    return gantt, avg_wt, avg_tat


# B. ROUND ROBIN SCHEDULING
# Python Program

def round_robin(processes, quantum):
    # processes = [(pid, burst)]
    queue = []
    for p in processes:
        queue.append([p[0], p[1]])  # pid, remaining burst

    time = 0
    gantt = []

    while queue:
        pid, burst = queue.pop(0)

        if burst > quantum:
            gantt.append((pid, time, time + quantum))
            time += quantum
            queue.append([pid, burst - quantum])
        else:
            gantt.append((pid, time, time + burst))
            time += burst

    return gantt
