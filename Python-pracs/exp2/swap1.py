a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("Before swap:\n numbers are",a,'and',b)
a=a+b
b=a-b
a=a-b
print("After swap:\n numbers are",a,'and',b)