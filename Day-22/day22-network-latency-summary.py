import json

def ask_for_filename():

    while True:

        clean_name = input("Enter the filename: ").strip()

        if clean_name == "":
            print("Name cannot be empty")
            continue

        else:
            break

    return clean_name



def loading_filename(filename):


    try:
        with open(filename, "r") as file:
            loaded_filename = json.load(file)

        if loaded_filename == []:
            print("No devices registered - Empty list.")
            return

    except FileNotFoundError:
        print("No devices registered")
        return 
    
    except json.JSONDecodeError:
        print("Invalid JSON. report cancelled.")
        return 


    return loaded_filename



def performance_and_calculation(loaded_files, threshold):

    count = 0
    total = 0

    for file in loaded_files:
        count = count + 1
        total = total + file["latency_ms"]

    average = total / count 

    site_investigation = []

    for file in loaded_files:

        if file["latency_ms"] > threshold:
            site_investigation.append(file)

    
    return (count, average, site_investigation)



def report(Site_count, latency_average, investigation):
    print(f'Total devices: {Site_count}')
    print(f'Average latency: {latency_average:.2f} ms')
    print("Devices to investigate:")
    if investigation == []:
        print("No devices need investigation")
    else:
        for file in investigation:
            print(file["name"])



def main():

    latency_threshold = 80

    file_name = ask_for_filename()
    loaded_files = loading_filename(file_name)

    if loaded_files is not None:
        Site_count, latency_average, investigation = performance_and_calculation(loaded_files, latency_threshold)
        report(Site_count, latency_average, investigation)

    else:
        return 

main()