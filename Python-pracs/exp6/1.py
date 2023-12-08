with open('T1.txt', 'w') as file:
    for i in range(10):
        number = input("Enter a number: ")
        file.write(f"{number}\n")

with open('T1.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

numbers.sort()

with open('T2.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")
