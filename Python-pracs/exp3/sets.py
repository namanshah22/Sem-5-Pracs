set1 = {'x', 'y', 'z', 'd', 'e'}  
print("Original set is:", set1)

# add() - adds an element to the set
print("add() function")
set1.add('f')  
print("Set after adding 'f':", set1)

# discard() – discards an element from the set
print("discard() function")
set1.discard('e')  
print("Set after discarding/updating 'e':", set1)

# remove() – removes an element from the set
print("remove() function")
set1.remove('x')  
print("Set after removing 'x':", set1)

# pop() - pops an arbitrary element from the set
print("pop() function")
set1.pop()  
print("Set after popping an element:", set1)

# clear() - clears the set
print("clear() function")
set1.clear()
print("Set after clearing:", set1)
