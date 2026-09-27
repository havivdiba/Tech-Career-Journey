
session_count = int(input("How many study sessions do you want to enter?: "))

session = 1
total_minutes = 0

while session < session_count:
    
    print("Session ", session)
    study_minutes = int(input("How many minutes did you study?: "))
    print()
    total_minutes = total_minutes + study_minutes
    session = session + 1 

average = round(total_minutes / (session-1), 2)

print("The total study minutes completed is ", total_minutes)
print("The average is :", average)