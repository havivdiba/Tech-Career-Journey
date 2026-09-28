def ask_servers_name():

    while True:

        name = input("Enter server name: ")
        name = name.strip()

        if name == "":
            print("Name cannot be empty")
            continue
        
        else:
            return name
            

def search_server_by_names(servers, names):

    for server in servers:

        if server["name"] == names:

            while True:
    
                try:
                    cpu_usage = int(input("Enter new CPU usage: "))

                    if cpu_usage < 0 or cpu_usage > 100:
                        print("CPU usage must be between 0 and 100")
                        continue
            
                    else:
                        return cpu_usage

                except ValueError:
                    print("Please Enter a whole number")
                    continue
            
    
    print("Server not found")
    return None 



def display_results(names, server_name, servers):

    if server_name is not None:
        for server in servers:
            if server["name"] == names:
                server["cpu_usage"] = server_name

        print(f'Updated {names} to {server_name}%.')
        print()


    print("Server inventory: ")

    for server in servers:
        print(f'{server["name"]} - CPU {server["cpu_usage"]}%')
    

        

def main():

    servers = [
        {"name": "web-01", "cpu_usage": 45},
        {"name": "db-01", "cpu_usage": 70},
        {"name": "api-01", "cpu_usage": 92}
    ]

    names = ask_servers_name()
    server_name = search_server_by_names(servers, names)
    display_results(names,server_name,servers)

main()

#
#print(names)