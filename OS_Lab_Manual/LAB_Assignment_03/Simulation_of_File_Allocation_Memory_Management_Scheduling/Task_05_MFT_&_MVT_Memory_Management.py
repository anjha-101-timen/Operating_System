# A. MFT (Multiple Fixed Tasks)
# Python Program

def MFT(partitions, process_size):
    for i in range(len(partitions)):
        if partitions[i] >= process_size:
            wasted = partitions[i] - process_size
            return i, wasted
    return None


# B. MVT (Multiple Variable Tasks)
# Python Program

def MVT(total_memory, process_sizes):
    allocations = []
    remaining = total_memory

    for size in process_sizes:
        if size <= remaining:
            allocations.append(size)
            remaining -= size
        else:
            allocations.append(None)

    return allocations, remaining
