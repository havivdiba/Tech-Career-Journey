student_name = input("What is the student's name? ")
study_hours = float(input("How many hours were completed? "))
practice_completed = input("Was the practice completed? yes or no? ")

if study_hours >= 4 and practice_completed == "yes":
    print("Excellent session \n")
elif study_hours >= 2 or practice_completed == "yes":
    print("Good session, but one requirement is missing.")
else:
    print("More study and practice are required")

print("\n Evaluation completed for: ", student_name)