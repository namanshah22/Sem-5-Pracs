for i in range(1, 6):
    if i == 3:
        print("Using continue at 3")
        continue
    if i == 4:
        print("Using break at 4")
        break
    if i == 2:
        print("Using pass at 2")
        pass
    print("Iteration:", i)
