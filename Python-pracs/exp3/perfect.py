def perfect(n): 
    sum = 0
    for i in range(1, int(n/2) + 1): 
        if n % i == 0:
            sum += i 
    if n == sum:
        return True
    else:
        return False
n = int(input('Enter the number:')) 
print(perfect(n))
