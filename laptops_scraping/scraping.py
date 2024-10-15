import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of GearVN laptop collection
url = "https://cellphones.com.vn/laptop.html"

# Fetch the page content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Lists to store scraped data
laptop_names = []
laptop_prices = []
laptop_links = []

# Extracting relevant data from the page
for product in soup.find_all('div', class_='product-info'):
    # print(product)
    # print('-------------------')
    # Get the laptop name
    name = product.find('strong', class_='product__name')
    if name:
        laptop_names.append(name.text.strip())

    # Get the laptop price
    price = product.find('div', class_='block-box-price')
    if price:
        laptop_prices.append(price.text.strip())
    
    # Get the laptop link
    link = product.find('a')
    if link:
        laptop_links.append("https://cellphones.com.vn/" + link['href'])

# Create a DataFrame to organize the scraped data
laptops_df = pd.DataFrame({
    'Name': laptop_names,
    'Price': laptop_prices,
    'Link': laptop_links
})

# Optionally, save the data to a CSV file
laptops_df.to_csv('xgear_laptops.csv', index=False)
