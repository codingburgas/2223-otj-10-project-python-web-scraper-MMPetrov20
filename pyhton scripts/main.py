import requests
from bs4 import BeautifulSoup
from menu import select_category
from url_modification import update_URL

URL = update_URL(select_category())

# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")

# print(results.prettify())