a=int(input('Enter a number:')) 
b=int(input('Enter a number:')) 
maximum = lambda a,b:a if a> b else b
print(f'{maximum(a,b)} is a maximum number')
