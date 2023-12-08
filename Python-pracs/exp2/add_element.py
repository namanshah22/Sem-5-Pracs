n = int(input("Enter the size of list : "))
l = list()
for i in range(n):
    l.append(int(input(f"Enter the {i} element : ")))
print("list :",l)

n = int(input("Enter the size of list : "))
s = set()
for i in range(n):
    s.add(int(input(f"Enter the {i} element : ")))
print("set :", s)

n = int(input("Enter size "))
t = tuple()
l = list(t)
for i in range(n):
    l.append(int(input(f"Enter the {i} element : ")))

t = tuple(l)
print("tuple :", t)