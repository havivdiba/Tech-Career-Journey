practice_minutes = [35, 50, 20, 45, 40]

total_minutes = 0
session_count = 0
goal_session_count = 0
longest_session = 0
shortest_session = 0


for spent_minutes in practice_minutes:
    total_minutes = total_minutes + spent_minutes
    session_count = session_count + 1

    if spent_minutes >= 30:
        goal_session_count = goal_session_count + 1

    if spent_minutes > longest_session:
        longest_session = spent_minutes

    if session_count == 1:
        shortest_session = spent_minutes
    elif spent_minutes < shortest_session:
        shortest_session = spent_minutes


if session_count > 0:
    average_minutes = total_minutes / session_count
    average_minutes = round(average_minutes, 2)

    goal_percentage = goal_session_count / session_count * 100
    goal_percentage = round(goal_percentage, 2)
else:
    average_minutes = 0
    goal_percentage = 0 


print("Total minutes :", total_minutes)
print("Session count :", session_count)
print("Average :", average_minutes)

if average_minutes >= 45:
    print("Excellent practice average")
elif average_minutes >= 30:
    print("Practice goal reached")
else:
    print("Practice goal not reached")

session_difference = longest_session - shortest_session
below_goal_count = session_count - goal_session_count

print("Sessions reaching 30 minutes:", goal_session_count)
print("Goal percentage:", goal_percentage, "%")

if goal_percentage >= 80:
    print("Strong consistency")
elif goal_percentage >= 50:
    print("Developing consistency")
else:
    print("Consistency needs improvement")
    
print("Longest session:", longest_session)
print("Shortest session:", shortest_session) 

print("Difference:", session_difference, "minutes")
print("Sessions below 30 minutes:", below_goal_count)