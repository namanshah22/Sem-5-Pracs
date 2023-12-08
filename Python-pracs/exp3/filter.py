arr = []
n = int(input('Enter the number of elements in the list:'))
print('Enter list elements:')
for i in range(n):
    arr.append(int(input()))

print('Original list:', arr)

arr2 = [x ** 3 for x in arr if x % 2 != 0]

print('The cube of odd elements in the list:', arr2)
