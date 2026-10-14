def investigation_speed(download_mbps, threshold_mbps):
    if download_mbps < threshold_mbps:
        return "Investigate"

    return "Acceptable"