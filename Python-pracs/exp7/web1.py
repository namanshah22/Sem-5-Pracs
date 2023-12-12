import re

with open('Sample.txt', 'r') as file:
    text = file.read()
    pattern = r'https?://\S+'
    websites = re.findall(pattern, text)
    print(websites)
