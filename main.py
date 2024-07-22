# Text extraction from official hotel website
# Saves extrated text in a txt file

import requests
from bs4 import BeautifulSoup

target_url = "https://www.landonhotel.com"

response = requests.get(target_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text()

    with open('website_text.txt', 'w') as text_file:
        text_file.write(text)

    print("Text extracted and saved successfully!")

else:
    print(f"Error: failed to retrice website content. Status code: {response.status_code}")
