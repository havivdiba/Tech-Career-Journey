#session_minutes = [30, 45, 20, 50]
weekdays_minutes = [30, 45, 20, 50]
weekend_minutes = [60, 40]

def calculate_weekly_total(period_minutes):
    total = 0
    session = 1
    
    for minutes in period_minutes:

        print("Day :", session)
         #minutes = int(input("How many minutes did you completed: "))
        print("How many minutes covered : ", minutes)
        print()
        total = total + minutes
        session = session + 1

    return total


weekday_total = calculate_weekly_total(weekdays_minutes)
weekend_total = calculate_weekly_total(weekend_minutes)
combined_total = weekday_total + weekend_total

#weekly_total = calculate_weekly_total(session_minutes)
#plus_bonus_time = weekly_total + 15

#print("Total Minutes completed: ", weekly_total)
#print("Total minutes + Bonus time of 15 min: ", plus_bonus_time)

print("The total weekday minutes are: ", weekday_total)
print("The total weekend minutes are: ", weekend_total)
print("The combined total minutes are: ", combined_total)

#print()
