tuple1 = (15, 25, 35, 55, 55, 75, 95, 85, 105)  
print("Original tuple:", tuple1)

# len() - length of tuple
print("len() function")
print("The length of tuple is:", len(tuple1))

# count() - repetition of element in tuple
print("count() function")
print("The count of 55 in tuple is:", tuple1.count(55))  

# index() - gives index of element in tuple
print("Index() function")
print("The index of 85 in tuple is:", tuple1.index(85))  

# sort() - sorts the elements in tuple (Note: Tuple is immutable, so we convert it to a list first)
print("sort() function")
sorted_tuple = tuple(sorted(list(tuple1)))  # Sorted the tuple and converted back to tuple
print("The sorted tuple is:", sorted_tuple)

# min() - gives the minimum element of tuple
print("min() function")
print("The minimum element of tuple is:", min(tuple1))

# max() - gives the maximum element of tuple
print("max() function")
print("The maximum element of tuple is:", max(tuple1))

# sum() - gives the sum of elements in tuple
print("sum() function")
print("The sum of elements in tuple is:", sum(tuple1))
