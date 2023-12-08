import re

file = open('Sample.txt','r') 
text = file.read()
pattern = r'[a-zA-z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+' 
email = re.findall(pattern,text)
print(email)
