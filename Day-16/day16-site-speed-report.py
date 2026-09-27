def find_the_names_of_sites_for_investigation (sites, threshold): 

    investigation_sites = []

    for site in sites:
        if site ["download_mbps"] < threshold and site ["download_mbps"] >= 0: 
            investigation_sites.append(site["name"]) 

    return investigation_sites


def calculate_average_valid_speed(sites):

    total_valid_speed = 0
    count_valid_speed = 0

    for site in sites:
        if site["download_mbps"] >= 0:
            total_valid_speed = total_valid_speed + site["download_mbps"]
            count_valid_speed = count_valid_speed + 1

    if count_valid_speed > 0:
        average_valid_speed = total_valid_speed / count_valid_speed
        return average_valid_speed
    else:
        average_valid_speed = None
        return average_valid_speed


def display_results(find, average, cut_off):

    print(f'Investigation threshold: {cut_off} Mbps')
    if find == []:
        print("No sites need investigation")
    else:
        print("The following sites need investigation : ")
        for site in find:
            print(site)

    print()
    print("The Average valid speed result : ")

    if average is None:
        print("No valid speeds")
    else:
        print(f'The average valid speed is : {average :.2f} Mbps')

def ask_for_threshold():

    while True:
        try:
            threshold = int(input("Please Enter the threshold speed : "))
    
            if threshold >= 0:
                break
            else:
                print("Threshold must be zero or higher")
                continue
                
        except ValueError:
            print("Please enter a whole number.")
            continue

    return threshold

def main():

    sites = [
        {"name": "site-p", "download_mbps": 0},
        {"name": "site-q", "download_mbps": 50},
        {"name": "site-r", "download_mbps": -1}
]

    cut_off = ask_for_threshold()
    find = find_the_names_of_sites_for_investigation(sites, cut_off)
    average = calculate_average_valid_speed(sites)
    display_results(find, average, cut_off)

    #print(average)

main()