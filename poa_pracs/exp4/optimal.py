def optimal(page_stream, num_frames):
    frame = [-1] * num_frames
    count1 = 0
    count2 = 0

    print("\nPage Stream")
    for i in range(len(page_stream)):
        flag = False
        for j in range(num_frames):
            if frame[j] == page_stream[i]:
                flag = True
                count2 += 1
                break

        if not flag:
            index = -1
            farthest = 0
            for j in range(num_frames):
                next_occurrence = -1
                for k in range(i + 1, len(page_stream)):
                    if frame[j] == page_stream[k]:
                        next_occurrence = k
                        break

                if next_occurrence == -1:
                    index = j
                    break

                if next_occurrence > farthest:
                    farthest = next_occurrence
                    index = j

            frame[index] = page_stream[i]
            count1 += 1

        print(f"{page_stream[i]}\t\t\t", end="")
        for j in range(num_frames):
            if frame[j] != -1:
                print(f"{frame[j]}\t", end="")
            else:
                print("\t", end="")
        print("H" if flag else "F")

    hit_ratio = count2 / len(page_stream)
    miss_ratio = count1 / len(page_stream)

    print(f"\n\nNo. of page hits = {count2}")
    print(f"No. of page faults = {count1}")
    print(f"Hit ratio = {hit_ratio}")
    print(f"Miss ratio = {miss_ratio}")

# Example usage
num_frames = int(input("Enter no of frames in main memory: "))
page_stream = list(map(int, input("Enter page stream: ").split()))

optimal(page_stream, num_frames)
