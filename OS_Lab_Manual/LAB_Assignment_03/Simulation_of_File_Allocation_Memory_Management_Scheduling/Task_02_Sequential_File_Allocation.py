def sequential_allocation(disk, file_name, file_size):
    for i in range(len(disk) - file_size + 1):
        # If a continuous free block is available
        if all(block == 0 for block in disk[i:i+file_size]):
            for j in range(i, i + file_size):
                disk[j] = file_name
            return i, i + file_size - 1

    return None
