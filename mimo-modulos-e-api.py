import requests

option = "people"
url = f"https://swapi.mimo.dev/api/{option}/"
try:
  response = requests.get(url)
  response.raise_for_status()

  data = response.json()
  print(f"Successfully fetched {len(data)} entities")
except requests.HTTPError as e:
  print(f"Error fetching data: {e}")

if data:
  for entity in data:
    print(entity["name"])
else:
  print("Unable to download data")