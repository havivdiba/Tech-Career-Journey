import json

def loading_site (filename):

    try:
        with open(filename, "r") as file:
            loaded_sites = json.load(file)

        return loaded_sites
    except FileNotFoundError:
        print("File not found. Empty Inventory is returned")
        return []

def save_sites(sites, filename):

    with open(filename, "w") as file:
        json.dump(sites, file, indent=4)


def main():

    loaded_sites = loading_site("sites.json")

    for site in loaded_sites:
        if site["name"] == "site-02":
            site["download_mbps"] = 38

    save_sites(loaded_sites, "sites.json")
    print(loaded_sites)


main()