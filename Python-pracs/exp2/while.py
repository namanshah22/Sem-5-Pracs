n = int(input("Enter the number : "))
num = n
fact = 1
while n!=0:
    fact *= n
    n = n-1 
print (f"factorial of {num} is {fact}") 