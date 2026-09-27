study_minutes = int(input("How many minutes did you study per session?: "))
study_session = int(input("How many session did you complete?: "))

total_minutes = study_minutes * study_session

print("The total study minutes completed is :", total_minutes)

if total_minutes >= 120:
    print("Study goal reached")
else:
    print("Study goal not reached")

