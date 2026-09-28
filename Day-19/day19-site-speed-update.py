def ask_for_site_name():

    while True:
        name = input("Enter site name: ")
        clean_name = name.strip()

        if clean_name == "":
            print("Name cannot be empty")
            continue
        else:
            return clean_name

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

    sites = [
        {"name": "site-01", "download_mbps": 45},
        {"name": "site-02", "download_mbps": 12},
        {"name": "site-03", "download_mbps": 80}
    ]
    
    name = ask_for_site_name()
    concerned_site = search_the_site_name(sites, name)

    update_site_speed(concerned_site)

    display_results(sites, speed_threshold)

main()
