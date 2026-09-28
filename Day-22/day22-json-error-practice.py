import json

def loading_site(filename):

    try:
        with open(filename , "r") as file:
            loaded_sites = json.load(file)
        return loaded_sites

    except FileNotFoundError:
        print("File doesnt exist. Empty list is returned")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON. Inventory could not be loaded")
        return None 


result = loading_site("invalid-sites-test.json")
print(result)