#book_scraping
import requests
from bs4 import BeautifulSoup

url = "https://bookstohome.in/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("li", class_="product")

with open("books_under_200.txt", "w") as file:

    file.write("Books Under ₹200\n")
    file.write("\n")

    for book in books:

        title = book.find("h2")
        price = book.find("span", class_="woocommerce-Price-amount")

        if title and price:

            book_name = title.get_text(strip=True)

            amount = price.get_text(strip=True)
            amount = amount.replace("₹", "").replace(",", "")

            
            amount = float(amount)

            if amount <= 200:
                file.write(f"{book_name}\n")
                print(book_name)
                file.write(f"Price : ₹{amount}\n")
                print(amount,"\n")
                file.write("\n")
print("Filtered books saved successfully.")
