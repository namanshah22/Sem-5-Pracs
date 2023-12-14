import xml.etree.ElementTree as ET

# Your XML data file
xml_file_path = 'data.xml'

# Parse XML
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Retrieve all food items and print their names
for food in root.findall('.//food'):
    name = food.find('name').text
    print(f"Food Name: {name}")
