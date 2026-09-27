server ={
    "name":"web-01", 
    "region":"canada-central",
    "cpu-usage": 65,
    "ip_address": "10.0.0.5"
}

print(server["name"])

server["cpu-usage"] = 85
server["status"] = "Warning" 

print(server)
print(server.get("ip_address", "Not assigned"))

for key, value in server.items():
    print(key, ":", value)

if "ip_address" in server:
    print(server["ip_address"])

else:
    print("IP address missing")
    server["ip_address"] = "10.0.0.5"

print(server)
