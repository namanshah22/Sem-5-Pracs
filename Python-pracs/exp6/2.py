with open('T1.txt', 'r') as file:
    words = [word.strip() for word in file]

words.sort()

with open('T2.txt', 'w') as file:
    for word in words:
        file.write(f"{word}\n")
