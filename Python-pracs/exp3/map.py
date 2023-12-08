list1 = []
list2 = []

def add(a, b):
    return a + b

n1 = int(input('Enter number of elements in list 1:'))
for i in range(0, n1):
    element1 = int(input())
    list1.append(element1)

print("List 1:", list1)

n2 = int(input('Enter number of elements in list 2:'))
for i in range(0, n2):
    element2 = int(input())
    list2.append(element2)

print("List 2:", list2)

result = list(map(add, list1, list2))
print('The sum of elements in lists:', result)

