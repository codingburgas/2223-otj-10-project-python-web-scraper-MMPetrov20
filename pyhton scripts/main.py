import requests
from bs4 import BeautifulSoup
from menu import select_category

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")

# print(results.prettify())

print(select_category())
