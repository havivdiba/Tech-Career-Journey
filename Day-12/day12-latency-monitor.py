
stop_limit = 100

def determine_value_of_valid_readings():

    latency_display = []
    valid_count = 1
    while True:

        try:
            data = int (input(f"Please enter reading {valid_count} between 0 and 2000 (Press -1 to stop): "))

        except ValueError:
            print("Invalid input")
            continue
        
        if data == -1:
            print("Collection has ended")
            break 
        if data < 0 or data > 2000:
            print("Invalid readings")
            continue
        else:
            latency_display.append(data)
            valid_count = valid_count + 1

    return latency_display

def calculate_total_latency(display):
    total = 0

    for data in display:
        total = total + data

    return total


def calculate_average_latency(complete_reading , number_of_valid_reading):

    if number_of_valid_reading > 0:
        average = round (complete_reading / number_of_valid_reading, 2)

        return average
    else:
        return 0

def determine_number_of_slow_readings(display, reading_limit):
    session = 0

    for data in display:
        if data > reading_limit:
            session = session + 1

    return session

def determine_network_status(slow_reading):

    if slow_reading == 0:
        return "Healthy"
    elif slow_reading == 1 or slow_reading == 2:
        return "Warning"
    else:
        return "Critical"


def display_the_complete_results(number_of_valid_reading, complete_reading, average_latency, slow_reading, reading_status ):

    print("The Number of valid readings are/is : ", number_of_valid_reading)
    print("The Total latency is : ", complete_reading)
    print("The average of the complete latency is : ", average_latency )
    print("The Number of slow readings is : ", slow_reading)
    print("Network Status : ", reading_status )


def network_latency_monitor(reading_limit):

    display = determine_value_of_valid_readings()
    complete_reading = calculate_total_latency(display)
    number_of_valid_reading = len(display)
    average_latency = calculate_average_latency(complete_reading, number_of_valid_reading)
    slow_reading = determine_number_of_slow_readings(display, reading_limit)
    reading_status = determine_network_status(slow_reading)
    display_the_complete_results(number_of_valid_reading, complete_reading, average_latency, slow_reading, reading_status)


network_latency_monitor(stop_limit)
