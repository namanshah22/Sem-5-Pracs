n = int(input("Enter the value of n: "))
fibonacci_sequence = [0, 1]
for i in range(2, n):
    next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_fibonacci)
print("Fibonacci Sequence up to the", n, "value:")
print(fibonacci_sequence)
