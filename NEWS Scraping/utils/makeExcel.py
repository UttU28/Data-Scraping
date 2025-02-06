import json
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

def exportMatchedToExcel():
    """Reads the JSON file and exports matched articles to an Excel file sorted by date."""
    with open('newsData.json', 'r', encoding='utf-8') as file:
        newsData = json.load(file)
    
    # Filter only matched=True articles
    matchedArticles = [article for article in newsData if article.get('matched')]
    
    # Sort by date (assuming date is in YYYY-MM-DD format)
    matchedArticles.sort(key=lambda x: x['date'])
    
    # Prepare data for DataFrame
    data = []
    for idx, article in enumerate(matchedArticles, start=1):
        data.append([idx, article['date'], article['title'], article['link']])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Sr No.', 'Date', 'Title', 'URL'])
    
    # Save to Excel
    excelFilename = "DataCentreNEWS.xlsx"
    with pd.ExcelWriter(excelFilename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    
    # Adjust column widths
    workbook = load_workbook(excelFilename)
    worksheet = workbook.active
    worksheet.column_dimensions[get_column_letter(3)].width = 50  # Set Title column width to 200
    workbook.save(excelFilename)
    
    print(f"Successfully saved {len(matchedArticles)} matched articles to {excelFilename}")

if __name__ == "__main__":
    exportMatchedToExcel()