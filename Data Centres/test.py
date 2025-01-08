from bs4 import BeautifulSoup
import json
import os

# Read the HTML file
with open('page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags with class 'ui card'
cards = soup.find_all('a', class_='ui card')

# Extract data and save it in a list
data = []
for card in cards:
    header = card.find(class_='header')
    description = card.find(class_='description')
    
    # Process description to retain spaces for <br> tags
    if description:
        description = description.decode_contents().replace('<div class="description">', '')
        description = description.replace('</div>', '')
        description = description.split('<img')[0]
        description = description.split('<br/>')
        print(description)
    # Add extracted data to the list
    data.append({
        'name': header.get_text(strip=True) if header else None,
        'providerName': description[0] if description else None,
        'fullAddress': " ".join(description[1:]) if description else None,
        'location': 'Mississippi'
    })

# Remove duplicates based on the 'name' field
if os.path.exists('aa.json'):
    with open('aa.json', 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
        if isinstance(existing_data, list):
            # Create a set of existing names
            existing_names = {item['name'] for item in existing_data if 'name' in item}
            # Filter out duplicates
            new_data = [item for item in data if item['name'] not in existing_names]
            data = existing_data + new_data

# Save the updated data to the JSON file
with open('aa.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Data has been extracted and saved to 'aa.json'.")
