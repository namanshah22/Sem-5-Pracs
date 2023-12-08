# append() - appends element to list
print("append() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.append(70) 
print("List After Appending 70:", list1)

# extend() - extends by adding on with new list
print("extend() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list2 = [444, 555]  
list1.extend(list2)
print("After extending to list2, the original list is:", list1)

# insert() – inserts element at a particular location
print("insert() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.insert(1, 25)  
print("List After Inserting 25 at index 1:", list1)

# pop() - pops element from list
print("pop() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.pop(1)  
print("List after popping from index 1:", list1)

# copy() - copies a list
print("copy() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list2 = list1.copy()
print("Copied list is:", list2)

# clear() - clears the list
print("clear() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.clear()  
print("List after clearing:", list1)
