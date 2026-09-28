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

def save_sites(sites, filename):

    with open(filename , "w") as file:
        json.dump(sites, file)


def ask_for_site_name():

    while True:
        name = input("Enter site name: ")
        clean_name = name.strip()

        if clean_name == "":
            print("Name cannot be empty")
            continue
        else:
            return clean_name

def ask_for_new_site_details(sites):

    new_site_name = ask_for_site_name()

    for site in sites:
        if new_site_name == site["name"]:
            print("Site already exists")        
            return 
        
    new_site_speed = ask_for_new_speed()

    new_site_details = {"name": new_site_name,
                        "download_mbps": new_site_speed

    }

    print(f'Added {new_site_name} with {new_site_speed} Mbps')
    

    return new_site_details

def search_the_site_name(sites, name):

    for site in sites:

        if site["name"] == name:
            return site

    return None


def ask_for_new_speed():

    while True:

        try:
            dl_speed = int(input("Enter download speed in Mbps: "))

            if dl_speed < 0:
                print("Speed cannot be negative.")
                continue
            else:
                return dl_speed

        except ValueError:
            print("Please enter a whole number")
            continue


def update_site_speed(concerned_site):

    if concerned_site is not None:
        speed = ask_for_new_speed()
    
        concerned_site["download_mbps"] = speed
        print(f'Updated {concerned_site["name"]} to {concerned_site["download_mbps"]} Mbps')
    
    else:
        print("Site not found")


def display_results(sites, speed_threshold):

    print()
    print("Site report:")
    for site in sites:
        if site["download_mbps"] < speed_threshold:
            print(f'{site["name"]} - {site["download_mbps"]} Mbps - Investigate')
        else:
            print(f'{site["name"]} - {site["download_mbps"]} Mbps - Acceptable')


def main():

    speed_threshold = 20
    actual_loaded_sites = loading_site("site-inventory.json")

    if actual_loaded_sites is None:
        return

    while True:

        print("1. Display site report")
        print("2. Update site speed")
        print("3. Exit ")
        print("4. Add a new site")

        option = input("Choose option: ").strip()

        if option == "1":

            if actual_loaded_sites == []:
                print("No sites registered")
            else:
                display_results(actual_loaded_sites, speed_threshold)

        elif option == "2":
                
            name = ask_for_site_name()
            concerned_site = search_the_site_name(actual_loaded_sites, name)

            update_site_speed(concerned_site)

            if concerned_site is not None:
                save_sites(actual_loaded_sites, "site-inventory.json")

            #display_results(sites, speed_threshold)

        elif option == "3":
            print("Goodbye")
            break

        elif option == "4":
            new_sites_dict = ask_for_new_site_details(actual_loaded_sites)
            

            if new_sites_dict is not None:
                actual_loaded_sites.append(new_sites_dict)
                save_sites(actual_loaded_sites, "site-inventory.json")

        else:
            print("Invalid Choice")

main()

