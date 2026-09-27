try:
    number_of_study = int(input("Please Enter the number of study : "))
    
    if number_of_study < 0:
        print("Minutes cannot be negative")
    else:
        print("Minutes accepted")

except ValueError:
    print("Number of Study can Only be a whole number")

print("Program finished")
    
