
def ask_number_of_servers():

    while True:
        
        try:
            number_of_servers = int(input("Please Enter the Number of servers to Test: "))

            if number_of_servers <= 0:
                print("The number should be of 1 or Higher")
                continue
            else:
                break

        except ValueError:
            print("The number should be a whole number")
            continue

    return number_of_servers

def ask_names_of_servers():

    while True:
        names_of_servers = input("Please Enter the Name of server to Test: ")
        names_of_servers = names_of_servers.strip()

        if names_of_servers == "":
            print("The name sould not be Empty")
            continue
        else:
            return names_of_servers

def ask_cpu_usage():

    while True:
        try:
            cpu_usage = int(input("Please Enter the site CPU Usage: "))

            if cpu_usage < 0 or cpu_usage > 100:
                print("Please Enter a number from 0 to 100 inclusive")
                continue
            else:
                return cpu_usage

        except ValueError:
            print("Please Enter a whole number")
            continue

def store_complete_list(server_count):

    complete_server_list = []
    count = 0 

    while count < server_count:
        servers_name = ask_names_of_servers()
        cpu_percent = ask_cpu_usage()

        dict_of_servers = {"name": servers_name,
                           "cpu_usage": cpu_percent
                        }
        complete_server_list.append(dict_of_servers)

        count = count + 1

    return complete_server_list


def average_cpu_usage(total_server_list, server_count):

    total = 0

    for dictionnary in total_server_list:

        total = total + dictionnary["cpu_usage"]

    if server_count > 0:
        average = total / server_count
    else:
        average = 0

    return average


def get_critical_servers(total_server_list, usage_percentage):

    Critical_server_list = []

    for dictionnary in total_server_list:

        if dictionnary["cpu_usage"] >= usage_percentage:
            Critical_server_list.append(dictionnary["name"])

    return Critical_server_list


def display_the_record(total_server_list, server_count, average_cpu, critical_servers):
    print("Registered servers: ")
    for dictionnary in total_server_list:
        print(f'{dictionnary["name"]}: {dictionnary["cpu_usage"]}%')

    print()
    print("Total servers: ", server_count)
    print()
    print(f'Average CPU usage: {average_cpu:.2f}%')
    print()
    print("Critical servers: ")
    
    if critical_servers == []:
        print("There are no critical server")
    else:
        for name in critical_servers:
            print(name)



def main():

    usage_percentage = 90

    server_count = ask_number_of_servers()
    total_server_list = store_complete_list(server_count)
    average_cpu = average_cpu_usage(total_server_list, server_count)
    critical_servers = get_critical_servers(total_server_list, usage_percentage)
    display_the_record(total_server_list, server_count, average_cpu, critical_servers)
    

main()