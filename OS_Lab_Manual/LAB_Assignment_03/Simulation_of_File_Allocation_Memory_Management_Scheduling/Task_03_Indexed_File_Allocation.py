import random

def indexed_allocation(disk, file_name, file_size):
    free_blocks = [i for i, b in enumerate(disk) if b == 0]

    if len(free_blocks) < file_size:
        return None

    index_block = random.choice(free_blocks)
    free_blocks.remove(index_block)

    allocated = random.sample(free_blocks, file_size)

    disk[index_block] = f"{file_name}-index"
    for b in allocated:
        disk[b] = file_name

    return index_block, allocated
