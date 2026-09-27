session = 1
total_minutes = 0

while session <= 3:
    minutes = int(input("Enter the minutes for each session: "))

    if minutes == 0:
        print("You are not serious!")
        break 

    if minutes < 10:
        print("Session too short. Please enter at least 10 minutes")
        continue

    total_minutes = total_minutes + minutes
    session = session + 1

print("Final completed minutes are :", total_minutes)