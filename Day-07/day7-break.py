total_minutes = 0

while True:
    session_times = int(input("How many minutes studied? :"))

    if session_times == 0:
        break 

    total_minutes = total_minutes + session_times

print("The total minutes completed are :", total_minutes )