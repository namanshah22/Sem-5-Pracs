import re

file = open('Sample.txt','r') 
text = file.read()
pattern = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+' 
names = re.findall(pattern,text) 
print(names)
