def worst_fit(memory_blocks, process_sizes):
    for process_id, process_size in enumerate(process_sizes):
        worst_fit_index = -1
        max_remaining_space = -1

        for i, block_size in enumerate(memory_blocks):
            if block_size >= process_size and block_size - process_size > max_remaining_space:
                worst_fit_index = i
                max_remaining_space = block_size - process_size

        if worst_fit_index != -1:
            memory_blocks[worst_fit_index] -= process_size
            print(f"Process {process_id} allocated to Block {worst_fit_index}")
        else:
            print(f"Process {process_id} of size {process_size} cannot be allocated.")

# Example Usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

worst_fit(memory_blocks, process_sizes)
