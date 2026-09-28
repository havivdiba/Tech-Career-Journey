def ask_servers_name():

    while True:
        name = input("Enter server name: ").strip()

        if name == "":
            print("Name cannot be empty")
            continue
        else:
            return name


def search_server_by_names(servers, requested_name):

    for server in servers:
        if server["name"] == requested_name:
            return server

    return None


def ask_for_cpu_usage():

    while True:
        try:
            cpu_usage = int(input("Enter new CPU usage: "))

            if cpu_usage < 0 or cpu_usage > 100:
                print("CPU usage must be between 0 and 100")
                continue
            else:
                return cpu_usage

        except ValueError:
            print("Please enter a whole number")
            continue


def display_results(servers):

    print()
    print("Server inventory:")

    for server in servers:
        print(f'{server["name"]} - CPU {server["cpu_usage"]}%')


def main():

    servers = [
        {"name": "web-01", "cpu_usage": 45},
        {"name": "db-01", "cpu_usage": 70},
        {"name": "api-01", "cpu_usage": 92}
    ]

    requested_name = ask_servers_name()
    matched_server = search_server_by_names(servers, requested_name)

    if matched_server is not None:
        cpu_usage = ask_for_cpu_usage()
        matched_server["cpu_usage"] = cpu_usage

        print(f"Updated {requested_name} to {cpu_usage}%.")
    else:
        print("Server not found")

    display_results(servers)


main()