import requests
import json

url = "https://anapioficeandfire.com/api/books"

response = requests.get(url)
books = response.json()

books_dict = {}

for book in books:
    books_dict[book["name"]] = {
        "pages": book["numberOfPages"],
        "date_of_release": book["released"],
        "ISBN": book["isbn"],
        "publisher": book["publisher"]
    }

# Save dictionary into JSON file
with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books_dict, file, indent=4)

print("Books dictionary saved to books.json")