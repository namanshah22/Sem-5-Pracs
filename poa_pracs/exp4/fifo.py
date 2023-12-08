num = int(input("Enter no of frames in main memory: "))
frame = [-1] * num

n = int(input("Enter no of pages to be executed: "))
page_stream = list(map(int, input("Enter page stream: ").split()))

check = 'F'
j = 0
count1 = 0
count2 = 0

print("\nPage Stream")
for i in range(n):
    for k in range(num):
        if frame[k] == page_stream[i]:
            check = 'H'
            count2 += 1

    if j < num and check != 'H':
        frame[j] = page_stream[i]
        j += 1
        count1 += 1
    elif j >= num and check != 'H':
        j = 0
        frame[j] = page_stream[i]
        j += 1
        count1 += 1

    print(f"{page_stream[i]}\t\t\t", end="")
    for k in range(num):
        if frame[k] != -1:
            print(f"{frame[k]}\t", end="")
        else:
            print("\t", end="")
    print(check)
    check = 'F'

hit_ratio = count2 / n
miss_ratio = count1 / n

print(f"\n\nNo. of page hits = {count2}")
print(f"No. of page faults = {count1}")
print(f"Hit ratio = {hit_ratio}")
print(f"Miss ratio = {miss_ratio}")
