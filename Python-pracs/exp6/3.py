with open('T1.txt', 'r') as file:
    words = [word.strip()[::-1] for word in file]

with open('T2.txt', 'w') as file:
    for word in words:
        file.write(f"{word}\n")
