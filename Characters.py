import requests
import pandas as pd

url = "https://anapioficeandfire.com/api/characters?pageSize=50"

characters_list = []

while url:
    response = requests.get(url)
    data = response.json()

    for character in data:
        characters_list.append({
            "Name": character["name"],
            "Number_of_Books": len(character["books"]),
            "TV_Series_Appearances": len(character["tvSeries"])
        })

    # Pagination handling
    url = response.links.get("next", {}).get("url")

# Sort by TV appearances
characters_list.sort(
    key=lambda x: x["TV_Series_Appearances"],
    reverse=True
)

# Convert to DataFrame
df = pd.DataFrame(characters_list)

# Export to Excel
df.to_excel("characters.xlsx", index=False)

print("Characters data saved to characters.xlsx")