minutes_covered = [30, 45, 20, 50]
set_goal = 120

def calculate_total(times_covered):
    total = 0
    for times in times_covered:
        total = total + times
    return total

def calculate_average(total_minutes, session_count):
    if session_count > 0:
        average_calculation = round(total_minutes / session_count , 2)
        return average_calculation
    else:
        return 0

def check_goal(total_minutes, goal_minutes):
    if total_minutes >= goal_minutes:
        return "Goal reached"
    else:
        return "Goal not reached"

def display_report(complete_performance, average, checking_goal):
    print("The total minutes covered are :", complete_performance )
    print("The average minutes is : ", average)
    print("Remark : ", checking_goal)

def run_tracker(minutes_list, goal_minutes = 120):
    complete_performance = calculate_total (minutes_list)
    number_of_session = len(minutes_list)
    average = calculate_average(complete_performance, number_of_session)
    checking_goal = check_goal(complete_performance, goal_minutes)
    display_report(complete_performance, average, checking_goal)

run_tracker([10, 20], 25)