import json 

def ask_for_filename():

    while True:

        filename = input("Please enter the requested filename: ")
        clean_filename = filename.strip()

        if clean_filename == "":
            print("Filename cannot be empty")
            continue
        
        return clean_filename

def loading_file(filename):

    try:
        with open(filename, "r") as file:
            loaded_file = json.load(file)
        return loaded_file
    
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return None


def validation_of_list(filename):

     
    if not isinstance(filename, list):
        print("Filename can only be a list")
        return False

    for dictionnary in filename:
        if not isinstance(dictionnary, dict):
            print("The list can only contains dictionnary")
            return False

        if not "name" in dictionnary or not "latency_ms" in dictionnary:
            print("Either name nor latency_ms is available in device")
            return False

        name = dictionnary["name"]

        if not isinstance(name, str):
            print("Name can only be a string")
            return False
        
        if name.strip() == "":
            print("Router name cannot be empty")
            return False

        latency = dictionnary["latency_ms"]


        if isinstance (latency, bool) or not isinstance(latency,(int, float)):
            print("Latency cannot be boolean/ can only be an int or decimal number")
            return False
    
        if latency < 0:
            print("Latency cannot be a negative number")
            return False

    return True


def ask_for_threshold():

    while True:

        try:
            threshold = int(input("Please ENTER the threshold latency: "))

            if threshold < 0:
                print("The Threshold value must be of 0 and above")
                continue

        except ValueError:
            print("Threshold must be a whole number")
            continue
        
        return threshold

def router_investigation(threshold, filename):

    router_to_investigate = []

    for router in filename:
        if router["latency_ms"] > threshold:
            router_to_investigate.append(router)

    return router_to_investigate

def total_and_average(loaded_filename):

    count = 0
    total_latency = 0
    for router in loaded_filename:
        count = count + 1
        total_latency = total_latency + router["latency_ms"]

    average_latency = total_latency / count 

    return (count, average_latency)

def investigation_percentage(router_to_investigate, loaded_filename):

    percentage = len(router_to_investigate)/len(loaded_filename) * 100

    return percentage


def report_results(threshold, count, average, router_to_investigate, percentage):

    report_data = {

        "threshold_ms": threshold,
        "total_devices": count,
        "average_latency_ms": round(average, 2),
        "devices_to_investigate": router_to_investigate,
        "investigation_percentage": round(percentage, 2)

    }

    return report_data

def saving_report_data(report_data, filename):

    with open(filename, "w") as file:
        json.dump(report_data, file, indent=4)

def display_results(threshold, count, average, router_to_investigate, percentage):

    print(f'The threshold entered is : {threshold}')
    print(f'The total routers available is : {count}')
    print(f'The average latency value is : {average:.2f}')

    if router_to_investigate == []:
        print("No devices to investigate")

    else:
        print("Routers to investigate")
        for router in router_to_investigate:
            print(f'{router["name"]} - {router["latency_ms"]} ms')

    print(f'The investigate percentage is {percentage:.2f} %')


def main():

    file_name = ask_for_filename()
    loaded_filename = loading_file(file_name)
    

    if loaded_filename == []:
        print("No devices registered")
        return
    if loaded_filename is None:
        print("File has an error")
        return 

    is_valid = validation_of_list(loaded_filename)
    
    if is_valid is False:
        return

    threshold = ask_for_threshold()
    router_to_investigate = router_investigation(threshold, loaded_filename)
    count, average = total_and_average(loaded_filename)
    percentage = investigation_percentage(router_to_investigate, loaded_filename)
    report_data = report_results(threshold, count, average, router_to_investigate, percentage)
    print(json.dumps(report_data, indent=4))
    saving_report_data(report_data, "latency-report.json")
    display_results(threshold, count, average, router_to_investigate, percentage)
    print("Report saved to latency-report.json")

main()