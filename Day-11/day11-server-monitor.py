response_times = [120, 250, 180, 310, 90]
slow_limit = 200

def determine_number_of_response(response_minutes):
    number_of_response = len(response_minutes)

    return number_of_response

def calculate_total_response(response_minutes):
    total = 0
    for minutes in response_minutes:
        total = total + minutes

    return total

def average_total_response(total_response, counting_number):

    if counting_number > 0:
        average = round (total_response / counting_number, 2)
        return average
    else:
        return 0

def counting_response(response_minutes, poor_limit):
    session = 0
    for minutes in response_minutes:
        if minutes > poor_limit:
            session = session + 1

    return session

def system_status(count):

    if count == 0:
        return "Healthy"
    elif count <= 2:
        return "Warning"
    else:
        return "Critical"

def display_results(counting_number, total_response, average_response, count, status):
    print("Number of checks minutes are : ", counting_number)
    print("Total number of response minutes are :", total_response)
    print("The average response is : ",average_response)
    print("The slow-response count are/is : ", count)
    print("System status : ", status)

def run_monitor(response_minutes, poor_limit):
    counting_number = determine_number_of_response(response_minutes)
    total_response = calculate_total_response(response_minutes)
    average_response = average_total_response(total_response, counting_number)
    count = counting_response(response_minutes, poor_limit)
    status = system_status(count)
    display_results(counting_number,total_response, average_response, count, status)

run_monitor([], 200)

    