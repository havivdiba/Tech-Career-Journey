def ask_numbers_of_sites():

    while True:
        
        try:
            amount_of_sites = int(input("How many sites do you want to record DL-speed measurements?: "))

            if amount_of_sites > 0:
                break
            else:
                print("Please enter a number - 1 or higher:")
                continue

        except ValueError:
            print("Please Enter a whole number : ")
            continue
            

    return amount_of_sites

def collect_sites(number_of_sites):

    sites = []
    count = 0



    while count < number_of_sites:
        names = input("Please enter the site name : ")
        site_speed = ask_for_site_speed()

        site = {
                "name": names,
                "download_mbps": site_speed                            
        }

        sites.append(site)

        count = count + 1

    return sites

def ask_for_site_speed():

    while True:
        try:
            speed = int(input("Please enter the site speed : "))
            if speed >= 0:
                break
            else:
                print("Please enter number of 0 or higner")
                continue
                
        except ValueError:
            print("Please Enter a whole number")
            continue

    return speed

def main():


    number_of_sites = ask_numbers_of_sites()
    print("You have entered number: ", number_of_sites)

    recorded_sites = collect_sites(number_of_sites)
    print("Recorded sites", recorded_sites)


main()