def summarize_servers(servers):

    total_servers = 0
    critical_servers = 0
    invalid_servers = 0
    total_cpu = 0
    valid_readings = 0

    for current_server in servers:

        total_servers = total_servers + 1

        if current_server["status"] == "Critical":

            critical_servers = critical_servers + 1 

        if current_server["status"] == "Invalid":

            invalid_servers = invalid_servers + 1

        if current_server["status"] != "Invalid":

            total_cpu = total_cpu + current_server["cpu_usage"]
            valid_readings = valid_readings + 1

    if valid_readings > 0:

        average_cpu = total_cpu / valid_readings 
    else:
        average_cpu = None

    return {

        "total_servers": total_servers,
        "critical_servers": critical_servers,
        "invalid_servers" : invalid_servers,
        "valid_readings" : valid_readings,
        "average_cpu" : average_cpu
   }

def determine_status(server):


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

def find_critical_names (servers):

    critical_server_names = []

    for current_server in servers:
        if current_server["status"] == "Critical":
            critical_server_names.append(current_server["name"])

    return critical_server_names

def display_critical_names(critical_names):

    print("Servers with critical status :")

    if critical_names == []:
        print("No critical servers found")
    else:
        for name in critical_names:
            print(name)

def display_summary(report):
    print()
    print("Server summary")
    print()
    print(f'Total servers: {report["total_servers"]}')
    print(f'Critical servers: {report["critical_servers"]}')
    print(f'Invalid servers: {report["invalid_servers"]}')
    print(f'The valid readings: {report["valid_readings"]}')

    if report["average_cpu"] is None: 

        print("Average valid CPU: No valid readings")
    else:
        print(f'The Average valid CPU: {report["average_cpu"]:.2f}%')


#def display_warning_servers(warning_servers):
    

def main():

    servers = [
        {"name": "web-01", "cpu_usage": 90},
        {"name": "db-01", "cpu_usage": 100},
        {"name": "api-01", "cpu_usage": 101},
        {"name": "backup-01", "cpu_usage": 89}
]

    for current_server in servers:
        current_server["status"] = determine_status(current_server)


        display_server(current_server)

    critical_names = find_critical_names(servers)
    print()
    display_critical_names(critical_names)
    
    report = summarize_servers(servers)
    display_summary(report)
    

main()







#servers = [
#    {"name": "web-01", "status": "Normal"},
#   {"name": "db-01", "status": "Critical"},
#    {"name": "api-01", "status": "Invalid"},
#    {"name": "backup-01", "status": "Critical"},
#    {"name": "cache-01", "status": "Warning"}
#]

