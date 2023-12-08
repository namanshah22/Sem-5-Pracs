def lru(page_stream, num_frames):
    frame = [-1] * num_frames
    flag = [0] * num_frames
    count1 = 0
    count2 = 0

    print("\nPage Stream")
    j = 0
    c = 0
    lru = 0
    for i in range(len(page_stream)):
        check = 'F'
        min_val = 1000

        for k in range(num_frames):
            if flag[k] < min_val:
                min_val = flag[k]
                lru = k

        for k in range(num_frames):
            if frame[k] == page_stream[i]:
                check = 'H'
                c += 1
                flag[k] = c
                count2 += 1

        if j < num_frames and check != 'H':
            frame[j] = page_stream[i]
            j += 1
            c += 1
            flag[j-1] = c
            count1 += 1
        elif j >= num_frames and check != 'H':
            frame[lru] = page_stream[i]
            c += 1
            flag[lru] = c
            count1 += 1

        print(f"{page_stream[i]}\t\t", end="")
        for k in range(num_frames):
            if frame[k] != -1:
                print(f"{frame[k]}\t", end="")
            else:
                print("\t", end="")
        print(check)

    hit_ratio = count2 / len(page_stream)
    miss_ratio = count1 / len(page_stream)

    print(f"\n\nNo. of page hits = {count2}")
    print(f"No. of page faults = {count1}")
    print(f"Hit ratio = {hit_ratio}")
    print(f"Miss ratio = {miss_ratio}")

# Example usage
num_frames = int(input("Enter no of frames in main memory: "))
page_stream = list(map(int, input("Enter page stream: ").split()))

lru(page_stream, num_frames)
