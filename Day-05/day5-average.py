study_minutes = [45, 45, 45, 45]
daily_goal = 30

total_minutes = 0
session_count = 0

for current_minutes in study_minutes:
    total_minutes = total_minutes + current_minutes
    session_count = session_count + 1

   
average_minutes = total_minutes / session_count
average_minutes = round(average_minutes, 2)   



print("Total minutes:", total_minutes)
print("Session_count:", session_count)
print("Average minutes:", average_minutes)

if average_minutes >= 45:
    print("Excellent study average")
elif average_minutes >= 30:
    print("Average goal reached")
else:
    print("Average goal not reached")