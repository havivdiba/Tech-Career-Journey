study_hours = float(input("How many hours did you study? "))
practice_completed = input("Did you complete the practice? yes/no: ")

if study_hours >=2 and practice_completed == "yes":
    print("Session succesfully completed.")
else:
    print("Session requirements are not complete.")