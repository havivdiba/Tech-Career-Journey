
def ask_for_site_name(): 

    while True:
        name = input("Please Enter the site name: ")
        clean_name = name.strip()

        if clean_name == "":
            print("Site name cannot be empty")
            continue
        else:
            return clean_name


def main():

    correct_name = ask_for_site_name()
    print(f'[{correct_name}]')

main()