from BTrees.IIBTree import IIBTree
import time
t = IIBTree()
#insertion_start_time = time.time()
#for i in range(1000):
#    t.update({i: 2*i})
#insertion_end_time = time.time()
#print(f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")

value = int(input("Enter Element to Insert : "))
insertion_start_time = time.time()
t.insert(value, value)
insertion_end_time = time.time()
print("Element inserted into the B tree.")
print(f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")


key = int(input("enter key: "))
search_start_time = time.time()
if t.has_key(key):
    print(t[key])
search_end_time = time.time()
print(f"Search time: {round((search_end_time-search_start_time)*1000,3)} milliseconds")