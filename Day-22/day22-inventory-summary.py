import json

def ask_for_json_filename():

    while True:

        name = input("Please Enter the File name: ")
        clean_name = name.strip()

        if clean_name == "":
            print("Empty response is not accepted ")
            continue
        else:
            return clean_name

def load_json_filename(filename):

        try:
            with open(filename, "r") as file:
                inventory = json.load(file)
            return inventory

        except FileNotFoundError:
            return []
        
        except json.JSONDecodeError:
            return None

def calculate_total_sites(loaded_inventory):

    count = 0
    total = 0
    for site in loaded_inventory:
        count = count + 1
        total = total + site["download_mbps"]

    average = total / count

    return (count, average)


def site_diagnostic(threshold, loaded_inventory):

    diagnostic_site = []

    for site in loaded_inventory:
        if site["download_mbps"] < threshold:
            diagnostic_site.append(site)

    return diagnostic_site


def display_results(total_site, average_calculation, Site_investigation):
    print(f'Total sites: {total_site}')
    print(f'Average download speed: {(average_calculation):.2f} Mbps')
    
    if Site_investigation == [] :
        print("No sites need investigation")
    else:
        print("Sites to investigate")
        for site in Site_investigation:
            print(f'{site["name"]}')

def main():

    threshold = 20
    inventory_name = ask_for_json_filename()

    loaded_inventory = load_json_filename(inventory_name)

    if loaded_inventory == []:
        print("No sites registered")
        return
    if loaded_inventory is None:
        print("The JSON file is invalid")
        return

    else:
        total_site, average_calculation = calculate_total_sites(loaded_inventory)
        Site_investigation = site_diagnostic(threshold, loaded_inventory)
        display_results(total_site, average_calculation, Site_investigation)

main()