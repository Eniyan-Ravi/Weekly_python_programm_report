#reading h2
import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/python/python-json/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all("h2")
hyp = soup.find_all("a")

print("H2 Headings:\n")

for i, heading in enumerate(headings, start=1):
    print(i,".",heading.get_text(strip=True))

for j, hyp in enumerate(hyp,start=1):
    print(hyp.get_text(strip=True))
