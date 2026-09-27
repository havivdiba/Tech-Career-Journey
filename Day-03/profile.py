name = input("What is the student's name?" )
learning_day = int(input("What is their current learning day?" ))
morning_study_hours = float(input("What are their morning study hours? "))
evening_study_hours = float(input("What are their evening study hours?" ))

total_hours = morning_study_hours + evening_study_hours

print("Student:", name)
print("Learning day:", learning_day)
print("Total hours:", total_hours)


