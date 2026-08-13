#parsing
import sys

print("Python executable:", sys.executable)
print("Python version:", sys.version)
from bs4 import BeautifulSoup

html = """
<html>
<body>

<h1>Hello</h1>

<p>Python Tutorial</p>

</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

#print(soup)

import requests

url = "https://www.geeksforgeeks.org/python/python-json/"

response = requests.get(url)
soupsd = BeautifulSoup(response.text, "html.parser")


#print(response.text)
print(soupsd.title.text)