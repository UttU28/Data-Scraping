from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.datacentermap.com/usa/california/los-angeles/"

# Set up Selenium with Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Replace 'path/to/chromedriver' with the path to your ChromeDriver
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the URL
    driver.get(url)

    # Wait until elements with class 'ui card' are present
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "ui.card"))
    )

    # Get the page source after JavaScript has loaded
    page_source = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all <a> tags with class 'ui card'
    cards = soup.find_all('a', class_='ui card')

    # Extract data and save it in a list
    data = []
    for card in cards:
        header = card.find(class_='header')
        description = card.find(class_='description')
        
        # Process description to retain spaces for <br> tags
        if description:
            description = description.decode_contents()
            description = description.split('<img')[0]
            description = description.split('<br/>')
        
        # Add extracted data to the list
        data.append({
            'name': header.get_text(strip=True) if header else None,
            'providerName': description[0].strip() if description else None,
            'fullAddress': " ".join([desc.strip() for desc in description[1:]]) if description and len(description) > 1 else None,
            'location': 'Mississippi'
        })

    # Print the extracted data
    for entry in data:
        print(entry)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
