import json

sites = [
        {"name": "site-01", "download_mbps": 45},
        {"name": "site-02", "download_mbps": 12},
        {"name": "site-03", "download_mbps": 80}
    ]

with open("site-inventory.json", "w") as file:
    json.dump(sites, file, indent=2)
