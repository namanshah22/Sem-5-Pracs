def best_fit(memory_blocks, process_sizes):
    for process_id, process_size in enumerate(process_sizes):
        best_fit_index = -1
        min_remaining_space = float('inf')

        for i, block_size in enumerate(memory_blocks):
            if block_size >= process_size and block_size - process_size < min_remaining_space:
                best_fit_index = i
                min_remaining_space = block_size - process_size

        if best_fit_index != -1:
            memory_blocks[best_fit_index] -= process_size
            print(f"Process {process_id} allocated to Block {best_fit_index}")
        else:
            print(f"Process {process_id} of size {process_size} cannot be allocated.")

# Example Usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

best_fit(memory_blocks, process_sizes)
