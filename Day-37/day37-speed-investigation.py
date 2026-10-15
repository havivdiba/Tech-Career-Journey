def investigation_speed(download_mbps, threshold_mbps):
    if download_mbps < threshold_mbps:
        return "Investigate"

    return "Acceptable"

print(investigation_speed(8, 15))
print(investigation_speed(15, 15))
print(investigation_speed(22, 15))