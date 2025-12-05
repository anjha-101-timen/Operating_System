def first_fit(blocks, process_size):
    for i in range(len(blocks)):
        if blocks[i] >= process_size:
            alloc = blocks[i]
            blocks[i] -= process_size
            return i
    return None

def best_fit(blocks, process_size):
    best_index = None
    best_size = 999999
    for i in range(len(blocks)):
        if 0 < blocks[i] >= process_size and blocks[i] < best_size:
            best_size = blocks[i]
            best_index = i
    if best_index is not None:
        blocks[best_index] -= process_size
    return best_index

def worst_fit(blocks, process_size):
    worst_index = None
    worst_size = -1
    for i in range(len(blocks)):
        if blocks[i] >= process_size and blocks[i] > worst_size:
            worst_size = blocks[i]
            worst_index = i
    if worst_index is not None:
        blocks[worst_index] -= process_size
    return worst_index
