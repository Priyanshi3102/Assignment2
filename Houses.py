import requests

url = "https://anapioficeandfire.com/api/houses?pageSize=50"

houses_data = []

while url:
    response = requests.get(url)
    data = response.json()

    for house in data:
        houses_data.append({
            "House": house["name"],
            "Region": house["region"]
        })

    # Pagination handling
    url = response.links.get("next", {}).get("url")

# Sort alphabetically
houses_data.sort(key=lambda x: x["House"])

# Write to text file
with open("houses.txt", "w", encoding="utf-8") as file:
    for house in houses_data:
        file.write(f'{house["House"]} - {house["Region"]}\n')

print("Data saved to houses.txt")