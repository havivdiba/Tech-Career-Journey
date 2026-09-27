def collect_cpu_readings():
    reading = []

    while True:
        usage = int(input("Please enter CPU usage from 0 to 100 : "))
        if usage == -1:
            break
        elif usage < 0:
            print("Value is invalid")
            continue
        elif usage > 100:
            print("Value is invalid")
            continue
        else:
            reading.append(usage)

    return reading

def calculate_average(readings):

    total = 0
    session = 0

    for usage in readings:
        total = total + usage 
        session = session + 1
       
    if session > 0:
        average_calculation = round (total / session , 2)
        return average_calculation
    else:
        return 0

def count_high_readings(readings, high_limit):
    session = 0

    for usage in readings:

        if usage > high_limit:
            session = session + 1
        
    return session

def determine_status(high_count):

    if high_count == 0:
        return "Healthy"
    elif high_count == 1:
        return "Warning"
    else:
        return "Critical"    

def display_report(number_of_reading, average, high_count, status):
    print("The number of valid readings are : ", number_of_reading)
    print("The average CPU usage is : ", average)
    print("The high-reading counts is : ", high_count)
    print("The status of the CPU : ", status)

def run_cpu_monitor(high_limit = 80):
    readings = collect_cpu_readings()
    number_of_reading = len(readings)
    average = calculate_average(readings)
    high_count = count_high_readings(readings, high_limit)
    status = determine_status(high_count)
    display_report(number_of_reading, average, high_count, status)

run_cpu_monitor()