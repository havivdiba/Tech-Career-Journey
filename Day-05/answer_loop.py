correct_answer = "python"
answer = ""

while answer != correct_answer:
    answer = input("Which programming language are you learning? ")

    if answer != correct_answer:
        print("Incorrect. Try again.")

print("Correct answer!")