
#for server in servers:
#    if server["cpu_usage"] >= 80:
#        server["status"] = "Warning"
#    else:
#        server["status"] = "Normal"

#    print(
 #   f'{server["name"]} - CPU: {server["cpu_usage"]}% - Status: {server["status"]}'
#)

def determine_status(server):

#    try:
#        cpu_usage = int(server["cpu_usage"])
#    except ValueError:
#        return "Invalid"

    if server["cpu_usage"] < 0 or server["cpu_usage"] > 100:
        return "Invalid"

    elif server["cpu_usage"] < 80:
        return "Normal"
    
    elif server["cpu_usage"] >= 80 and server["cpu_usage"] < 90:
        return "Warning"
    
    else:
        return "Critical"

def display_server(server):
    print(f'{server["name"]} - CPU {server["cpu_usage"]}% - Status: {server["status"]}')

def main ():
    servers = [
    {"name": "web-01", "cpu_usage": -1},
    {"name": "db-01", "cpu_usage": 0},
    {"name": "api-01", "cpu_usage": 100},
    {"name": "api-01", "cpu_usage": 101}
]
    
    critical_count = 0
    invalid_count = 0
    
    for current_server in servers:
        current_server["status"] = determine_status(current_server)     
        display_server(current_server)

        if current_server["status"] == "Critical":
            critical_count = critical_count +1
        if current_server["status"] == "Invalid":
            invalid_count = invalid_count + 1

    print("The critical-server count is : ", critical_count)
    print("The number of invalid-count is : ", invalid_count)


main()