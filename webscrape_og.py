import requests
from bs4 import BeautifulSoup
import mysql.connector

# Function to scrape data from e-commerce websites
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        watches = []
        for product in soup.find_all('div', class_='_1AtVbE'):
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

# Connect to MySQL database using mysql-connector-python
# Replace 'username', 'password', 'host', and 'database_name' with your actual database credentials
conn = mysql.connector.connect(
    
)
cursor = conn.cursor()

# Execute this SQL command to create the 'products' table
create_table_query = """
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price VARCHAR(50) NOT NULL
)
"""

cursor.execute(create_table_query)

# Iterate through the URLs and scrape data
for url in urls:
    data = scrape_website(url)
    if data:
        # Insert scraped data into the 'products' table in the database
        insert_query = "INSERT INTO products (title, price) VALUES (%s, %s)"
        for product in data:
            cursor.execute(insert_query, (product['name'], product['price']))
            conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
