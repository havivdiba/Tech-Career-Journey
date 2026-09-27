weekday_minutes = []
weekend_minutes = []

def calculate_weekly_minutes(period_label, list_minutes):

    total = 0
    session = 1

    for minutes in list_minutes:
        print(period_label," - Day:", session)
        print("How many minutes did you cover? :", minutes)
        print()
        session = session + 1
        total = total + minutes

    return total

def calculate_average(total_minutes, number_of_session):
    
    if number_of_session > 0:
        average = round (total_minutes / number_of_session, 2)
        return average
    else:
        return 0


weekday_total = calculate_weekly_minutes("Weekday", weekday_minutes)
weekend_total = calculate_weekly_minutes("Weekend", weekend_minutes)

combined_total = weekday_total + weekend_total

session_count = len(weekday_minutes) + len(weekend_minutes)

weekly_average = calculate_average(combined_total, session_count)

print("The combined total minutes for the week is : ", combined_total)
print("The weekly average minutes studied is :", weekly_average)
print()

