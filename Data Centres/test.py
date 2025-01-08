# import json
# import requests
# from bs4 import BeautifulSoup

# def makeRequest(url):
#     try:
#         # Ensure the URL is complete
#         full_url = f"https://www.datacenters.com{url}"
        
#         response = requests.get(full_url)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         # Set the encoding explicitly
#         response.encoding = response.apparent_encoding

#         soup = BeautifulSoup(response.content, 'html.parser')

#         div_content = soup.find_all('div', class_='LocationShowSidebar__sidebarData__RS15t')

#         for div in div_content:
#             getPhone = div.find('span', id='sidebarPhone')
#             if getPhone:
#                 return div.text.replace('Phone', '').strip()
#         return "No phone information found."
    
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred while making the request: {e}")
#         return None

# # Input and output file paths
# input_file = 'data.json'
# output_file = 'providers.json'

# try:
#     # Read the input JSON file
#     with open(input_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)
    
#     providers_dict = {}

#     for entry in data:
#         provider_name = entry['providerName']
#         url = entry['url']

#         # Fetch the phone information and add it to the entry

#         if provider_name not in providers_dict:
#             phone = makeRequest(url)
#             print(provider_name, phone)
#             entry['phone'] = phone
#             providers_dict[provider_name] = {
#                 "url": url,
#                 "phone": phone
#             }

#     # Write the resulting dictionary to a new JSON file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(providers_dict, file, indent=4)
    
#     print(f"Provider data has been saved to '{output_file}'.")

# except Exception as e:
#     print(f"An error occurred: {e}")


import json

# File paths
input_data_file = 'data.json'
providers_file = 'providers.json'
output_data_file = 'updated_data.json'

try:
    # Read the providers JSON file
    with open(providers_file, 'r', encoding='utf-8') as file:
        providers = json.load(file)
    
    # Read the input data JSON file
    with open(input_data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Add phone numbers to the data entries
    for entry in data:
        provider_name = entry['providerName']
        if provider_name in providers:
            entry['phone'] = providers[provider_name]['phone']
        else:
            entry['phone'] = "Phone not found"  # Add a default value if provider not in providers.json

    # Write the updated data to a new JSON file
    with open(output_data_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    
    print(f"Updated data has been saved to '{output_data_file}'.")

except Exception as e:
    print(f"An error occurred: {e}")
