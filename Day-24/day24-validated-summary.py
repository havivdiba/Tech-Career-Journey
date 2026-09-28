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

def ask_for_threshold():

    while True:

        try:
            requested_threshold = int(input("Please enter the threshold in Mbps: "))

            if requested_threshold < 0:
                print("Please enter a whole number of zero or above")
                continue

        except ValueError:
            print("Please enter a whole number")
            continue
        
        return requested_threshold


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
            print(f'Download speed for {site["name"]} must be a number.')
            return False

        if speed < 0:
            print(f'Download speed for {site["name"]} must be zero or above.')
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
            print("The JSON file not found")
            return []
        
        except json.JSONDecodeError:
            print("The JSON file is invalid")
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

def find_fastest_site(inventory):

    fastest_site = inventory[0]

    for site in inventory:
        if site["download_mbps"] > fastest_site["download_mbps"]:
            fastest_site = site

    return fastest_site


def find_slowest_site(inventory):

    slowest_site = inventory[0]

    for site in inventory:
        if site["download_mbps"] < slowest_site["download_mbps"]:
            slowest_site = site

    return slowest_site


def collect_report_data(threshold, total_site, average_calculation, fastest_site, slowest_site, site_investigation):

    percentage = (len(site_investigation) / total_site ) * 100

    report_data = {

        "threshold_mbps": threshold,
        "total_sites": total_site,
        "average_download_mbps": round(average_calculation,2),
        "fastest_site": fastest_site,
        "slowest_site": slowest_site,
        "sites_to_investigate": site_investigation,
        "investigation_percentage": round(percentage, 2)
    }
    return report_data

def save_report(report_data, filename):

    with open(filename, "w") as file:
        json.dump(report_data, file, indent=4)
        


def display_results(threshold, total_site, average_calculation, Site_investigation, fastest_site, slowest_site):
    print(f'The chosen threshold is: {threshold} Mbps')
    print(f'Total sites: {total_site}')
    print(f'Average download speed: {(average_calculation):.2f} Mbps')
    
    if Site_investigation == [] :
        print("No sites need investigation")
    else:
        print("Sites to investigate")
        for site in Site_investigation:
            shortfall = threshold - site["download_mbps"]
            print(f'{site["name"]} - {site["download_mbps"]} Mbps - {shortfall} Mbps below threshold')

    print(f'Fastest site: {fastest_site["name"]} - {fastest_site["download_mbps"]} Mbps')
    print(f'Slowest site: {slowest_site["name"]} - {slowest_site["download_mbps"]} Mbps')

    percentage = (len(Site_investigation) / total_site ) * 100

    print(f'Percentage of site to investigate is {percentage:.2f} %')

    
def main():
    
    inventory_name = ask_for_json_filename()

    loaded_inventory = load_json_filename(inventory_name)

    if loaded_inventory == []:
        print("No sites registered")
        return
    if loaded_inventory is None:
        print("Report cancelled.")
        return

    threshold = ask_for_threshold()
    total_site, average_calculation = calculate_total_sites(loaded_inventory)
    Site_investigation = site_diagnostic(threshold, loaded_inventory)
    fastest_site = find_fastest_site(loaded_inventory)
    slowest_site = find_slowest_site(loaded_inventory)
    report_data = collect_report_data(threshold, total_site, average_calculation, fastest_site, slowest_site, Site_investigation)
    print(json.dumps(report_data, indent=4))
    save_report(report_data, "summary-report.json")
    display_results(threshold, total_site, average_calculation, Site_investigation, fastest_site, slowest_site)
    print("Report saved to summary-report.json")  
        
main()


