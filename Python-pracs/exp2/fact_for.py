x=int(input("Enter number "))
fact = 1
if x <0:
    print("factorial is not for negative numbers")
elif x==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,x+1):
       fact =fact*i
print(f"Factorial of {x} is {fact}")