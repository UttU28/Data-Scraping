import pandas as pd

# Sample data
data = [
    ['Adolfo Contreras Contreras', '', 'Speaker Pass', '', 'EB MEETING', '', '-— Information', '', 'Position', 'Senior Business development Advisor', '', 'Company', 'Blockstream', '', 'Country', 'Spain', '', 'Company Category', 'Layer 1/ Layer 2 / Blockchain Foundation', '', ''],
    ['Adria Alsina Leal', '', 'General Pass', '', 'EB MEETING', '', '-— Information', '', 'Position', 'Professor', '', 'Company', 'Universitat de Vic', '', 'Country', 'Spain', '', 'Company Category', 'Other', '', ''],
    ['Adrian Vacas', '', 'General Pass', '', 'EB MEETING', '', '-— Information', '', 'Position', 'Profesional Gamer & Creator Content', '', 'Company', 'Vacas.Onchain', '', 'Country', 'Spain', '', 'Company Category', 'NFT / Gaming / Metaverse', '', ''],
    ['ADRIAN SASTRE DIAZ', '', 'General Pass', '', 'EB MEETING', '', '-— Information', '', 'Position', 'Influencer', '', 'Company', 'Pobremillenial', '', 'Country', 'Spain', '', 'Company Category', 'Other', '', '']
]

# Extract the relevant information
extracted_data = []
for entry in data:
    full_name = entry[0]
    position_index = entry.index('Position') + 1  # Get the position text right after 'Position'
    company_index = entry.index('Company') + 1    # Get the company text right after 'Company'
    
    position = entry[position_index] if position_index < len(entry) else None
    company = entry[company_index] if company_index < len(entry) else None
    
    extracted_data.append([full_name, position, company])

# Create a DataFrame
df = pd.DataFrame(extracted_data, columns=['Full Name', 'Position', 'Company'])

# Save to Excel
output_file = 'output_data.xlsx'
df.to_excel(output_file, index=False)

print(f'Data has been saved to {output_file}')
