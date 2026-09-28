import json


def validate_inventory(inventory):

    if not isinstance(inventory, list):
        print("A list is expected")
        return False

    for site in inventory:
        if not isinstance(site, dict):
            print("A dictionnary is expected")
            return False

        if not "name" in site or not "download_mbps" in site:
            print("Either name or download_mbps keys are not in site")
            return False

        speed = site["download_mbps"]

        if isinstance(speed, bool) or not isinstance(speed, (int, float)):
            print("Download speed must be a number.")
            return False

        if speed < 0:
            print("Download speed must be zero or above.")
            return False

        name = site["name"]

        if not isinstance(name, str ):
            print("Name can only be a string")
            return False

        if name.strip() == "":
            print("Name cannot be empty")
            return False
    
    return True


def load_json_filename(filename):

    try:
        with open(filename, "r") as file:
            inventory = json.load(file)
            is_valid = validate_inventory(inventory)

            if is_valid is False:
                return None

        return inventory

    except FileNotFoundError:
        print("File not found. Starting with an empty inventory.")
        return []
    
    except json.JSONDecodeError:
        print("Invalid JSON. Inventory could not be loaded.")
        return None


def main ():

    filename = input("Enter filename: ").strip()
    inventory_file = load_json_filename(filename)

    if inventory_file is None:
        print("Report cancelled.")
        return
    else:
        print(inventory_file)
        return 

main()


print("String:", validate_inventory([
    {"name": "site-01", "download_mbps": "45"}
]))
print("Boolean:", validate_inventory([
    {"name": "site-01", "download_mbps": True}
]))
print("Negative:", validate_inventory([
    {"name": "site-01", "download_mbps": -1}
]))
print("Zero:", validate_inventory([
    {"name": "site-01", "download_mbps": 0}
]))
print("Decimal:", validate_inventory([
    {"name": "site-01", "download_mbps": 12.5}
]))

print("Number:", validate_inventory([
    {"name": 123, "download_mbps": 45}
]))

print("Spaces:", validate_inventory([
    {"name": "   ", "download_mbps": 45}
]))

print("Valid:", validate_inventory([
    {"name": "site-01", "download_mbps": 0}
]))

# print("A:", validate_inventory([]))
# print("B:", validate_inventory({"name": "site-01", "download_mbps": 45}))
# print("C:", validate_inventory([
#     {"name": "site-01", "download_mbps": 45},
#     "site-02"
# ]))

# print("D:", validate_inventory([
#     {"name": "site-01", "download_mbps": 45},
#     {"name": "site-02"}
# ]))

# print("E:", validate_inventory([
#     {"name": "site-01", "download_mbps": 45},
#     {"name": "site-02", "download_mbps": 12}
# ]))
    