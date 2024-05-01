import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from e-commerce websites
def scrape_website(url):
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
# Extract data from the webpage
        # Replace this with your specific scraping logic based on the website's structure
        watches=[]
        for product in soup.find_all('div', class_='_1AtVbE'):
            print(product)
            name_elem = product.find('a', class_='IRpwTa')
            price_elem = product.find('div', class_='_30jeq3')
            if name_elem and price_elem:
                name = name_elem.text.strip()
                price = price_elem.text.strip()
                watches.append({'name': name, 'price': price})

        return watches
    else:
        print(f"Failed to fetch data from {url}")
        return None

# URLs of e-commerce websites to scrape
urls = ['https://www.flipkart.com/search?q=watches']

# Output file path
output_file = 'watches.csv'

with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'price'])
    writer.writeheader()

    for url in urls:
        data = scrape_website(url)
        if data:
            for product in data:
                writer.writerow(product)

print(f"Scraped data has been saved to {output_file}")

