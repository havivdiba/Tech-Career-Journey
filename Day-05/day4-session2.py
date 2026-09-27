total_minutes = 0
session_count = 0

for current_minutes in [30, 25, 40, 15]:
    total_minutes = total_minutes + current_minutes
    session_count = session_count + 1

    print("Running total: ", total_minutes)
    print("counting: ", session_count)

print(f"Final total is {total_minutes}")
print("Total count: ", session_count)
