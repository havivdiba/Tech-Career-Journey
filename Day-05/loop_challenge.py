student_name = input("What is the student's name?: ")
total_hours = 0

for days in range(1, 4):
    print("Day: ", days)
    study_hours = float(input("What is the number of hours studied for it? "))
    

    total_hours = total_hours + study_hours


print("Student: ", student_name)
print("Total hours: ", total_hours)


if total_hours >= 6:
    print("Three-day target achieved.")
else:
    print("Three-day target not achieved yet.")


print(f"You are {age} years old ")






