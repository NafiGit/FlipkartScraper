from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=laptop'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    with open('output.html', 'w') as file:
        file.write(soup.prettify())




# Find all the div elements with class="hCKiGj"
items = soup.find_all('div', class_='hCKiGj')

for item in items:
    # Extract information like brand, title, price, etc.
    brand = item.find('div', class_='syl9yP').text
    title = item.find('a', class_='WKTcLC').text
    price = item.find('div', class_='hl05eU').find('div', class_='Nx9bqj').text

    print(f"Brand: {brand}\nTitle: {title}\nPrice: {price}\n")




