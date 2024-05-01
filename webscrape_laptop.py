from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=laptop'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    with open('output.html', 'w') as file:
        file.write(soup.prettify())





# Find all <section> tags within the provided HTML content
sections = soup.find_all('section')

# Extract and print the text content of each <section> tag
for section in sections:
    feature_name = section.find('div', class_='fxf7w6 rgHxCQ').text.strip()
    print(feature_name)


