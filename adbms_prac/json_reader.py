import json

# Your JSON data file
json_file_path = 'data.json'

# Read JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Print information for each item in the JSON
for item in data:
    name = item['name']
    location = item['location']
    country = item['country']

    print(f"Name: {name}")
    print(f"Location: {location}")
    print(f"Country: {country}")
  
