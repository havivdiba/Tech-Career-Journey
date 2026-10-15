def investigation_speed(download_mbps, threshold_mbps):
    
    if download_mbps < 0 or threshold_mbps < 0:
        return "Invalid"
    
    if download_mbps < threshold_mbps:
        return "Investigate"

    return "Acceptable"

print(investigation_speed(8, 15))
print(investigation_speed(15, 15))
print(investigation_speed(22, 15))

print(investigation_speed(-10, 15))
print(investigation_speed(20, -5))
print(investigation_speed(0, 15))
print(investigation_speed(15, 15))