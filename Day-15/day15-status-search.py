
def find_server_names_by_status(servers, target_status):
    warning_server_list = []

    for current_server in servers:
        if current_server["status"] == target_status:
            warning_server_list.append(current_server["name"])

    return warning_server_list

def display_warning_servers(warning_server_names):
    print("Servers with Warning status are: ")

    for names in warning_server_names:
        print(names)

def main ():

    servers = [
        {"name": "web-01", "status": "Warning"},
        {"name": "db-01", "status": "Critical"},
        {"name": "api-01", "status": "Invalid"},
        {"name": "backup-01", "status": "Warning"},
        {"name": "cache-01", "status": "Normal"}
]

    warning_server_names = find_server_names_by_status(servers, "Warning")
    print()
    display_warning_servers(warning_server_names)

main()