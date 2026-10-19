def classify_rsrp(rsrp):

    if rsrp >= -80:
        return "Excellent"
    elif rsrp >= -90 and rsrp < -80:
        return "Good"
    elif rsrp >= -100 and rsrp < -90:
        return "Fair"
    else:
        return "Poor"


def main ():

    try:
        rsrp = float(input("Please enter any RSRP Value in dB : "))
        results = classify_rsrp(rsrp)
        print(results)

    except ValueError:
        print("Invalid RSRP input")




main()
