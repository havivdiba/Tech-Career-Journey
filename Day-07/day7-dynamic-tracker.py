study_session = int(input("How many study sessions do you want?: "))
session = 1
total_minutes = 0

while study_session < 0:
    study_session = int(input("Invalid number. Please enter 0 or more sessions: "))

while session <= study_session:
    print("Session :", session)
    session_minutes = int(input("How many minutes?: "))

    while session_minutes < 0:
        session_minutes = int(input("Inalid number. Please enter 0 or more minutes: "))

    total_minutes = total_minutes + session_minutes
    session = session + 1

if study_session > 0:
    average = round(total_minutes / study_session, 2)
else:
    average = 0

print("The final total minutes are :", total_minutes)
print("The average minutes is :", average)