def get_number_of_sites():

    while True:

        try:
            number_of_sites = int(input("Please Enter the number of sites to Test : "))
            if number_of_sites > 0:
                break
            else:
                print("Please Enter a number going between 1 and higher")
                continue

        except ValueError:
            print("Please Enter a whole number")
            continue
        
    return number_of_sites


def get_investigation_threshold():

    while True:
        try:
            threshold = int(input("Please Enter the threshold Speed in Mbps : "))
            if threshold >= 0:
                break
            else:
                print("Invalid Number | Please Enter a valid number")
                continue

        except ValueError:
            print("Please Enter a whole number")
            continue
        
    return threshold

def ask_for_sites_name(total_number_of_sites):

    sites_name_speed = []


    count = 0

    while count < total_number_of_sites:
        site = input("Please Enter the name of the site : ")
        speed_test = ask_for_sites_speed()
        count = count + 1

        dict_of_sites = {"name": site,
                         "download_mbps": speed_test
        }

        sites_name_speed.append(dict_of_sites)

    return sites_name_speed

def ask_for_sites_speed():

    while True:

        try:
            speed = int(input("Please Enter the Speed for the site : "))

            if speed >= 0:
                break
            else:
                print("Please Enter a number from 0 to higher")
                continue
            
        except ValueError:
            print("Please Enter a whole number")
            continue

    
    return speed
           

def site_investigation(site_list, threshold):

    investigation_sites_list = []

    for current_site in site_list:

        if current_site["download_mbps"] < threshold:

            investigation_sites_list.append(current_site["name"])

    return investigation_sites_list



def average_speed_test(site_list, total_number_of_sites):

    total = 0
    for current_site in site_list:
        total = total + current_site["download_mbps"]

    if total_number_of_sites > 0:
        average_value = total / total_number_of_sites
    else:
        average_value = 0

    return average_value


def display_results(threshold, site_list, total_number_of_sites, average, investigation):

    print(f'Investigation threshold: {threshold} Mbps' )
    print()
    print("Recorded sites: ")
    for current_site in site_list:
        print(f'{current_site["name"]} : {current_site["download_mbps"]} Mbps')

    print()
    print("Total sites: ", total_number_of_sites)
    print(f'Average speed: {average:.2f} Mbps')
    print()
    print("Sites needing investigation")
    if investigation == []:
        print("No sites need investigation")
    else: 
        for current_name in investigation:
            print(current_name)


def main():


    total_number_of_sites = get_number_of_sites()
    limit = get_investigation_threshold()
    site_list = ask_for_sites_name(total_number_of_sites)
    investigation = site_investigation(site_list, limit)
    #sites_speed_list = ask_for_sites_speed()
    average = average_speed_test(site_list, total_number_of_sites)
    display_results(limit, site_list, total_number_of_sites, average,investigation)

main()



