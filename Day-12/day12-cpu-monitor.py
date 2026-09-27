latency_readings = []

def determine_number_of_valid_readings(latency_display):
    total = 0
    number_of_reading = 0

    for data in latency_display:
        data = int (input("Please enter the readings between 0 and 2000 (Press -1 to stop): "))

        if data == -1:
            print("Collection has ended")
            break 
        if data < 0 or data > 2000:
            print("Invalid readings")
            continue

        
