study_sessions = [25, 45, 10, 60, 30]

total_minutes = 0
total_sessions = 0

goal_session = 0
failed_goal_session = 0

for session_times in study_sessions:
    total_minutes = total_minutes + session_times
    total_sessions = total_sessions + 1

    if session_times >= 30:
        goal_session = goal_session + 1


    if session_times < 30:
        failed_goal_session = failed_goal_session + 1

if total_minutes >= 150:
    print("Practice goal reached")
else:
    print("Practice goal not reached")

if total_sessions > 0:
    average_minutes = total_minutes / total_sessions
else:
    average_minutes = 0

print("The total number of study minutes is:", total_minutes,"min")
print("The total number of sessions is:", total_sessions)
print("The average number of min/sessionis:", average_minutes, "min")
print("No of sessions at least 30 min:", goal_session)
print("No of sessions less than 30 min:", failed_goal_session)
