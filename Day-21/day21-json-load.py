import json

with open("sites.json", "r") as file:
    loaded_sites = json.load(file)

print(loaded_sites)