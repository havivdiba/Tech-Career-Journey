total_minutes = 0
completed_days = 0

while total_minutes < 120:
    total_minutes = total_minutes + 30
    completed_days = completed_days + 1

    print("Completed day:", completed_days)
    print("Running total:", total_minutes)

print("Final Total minutes:" completed_days)
print("All days completed:", completed_days)



minutes = 10
session = 1

while minutes < 50:
    print("Session:", session)
    print("Minutes:", minutes)

    minutes = minutes + 10
    session = session + 1

print("Final minutes:", minutes)
print("Final session:", session)