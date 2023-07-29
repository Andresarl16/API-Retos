import requests

response = requests.get(
    "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json")
data = response.json()

for country in data:
    country["location_states"].sort(
        key=lambda x: x["state_name"])

print(data)
