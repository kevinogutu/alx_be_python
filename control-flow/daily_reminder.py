# Prompt for a Single Task

task = input("Enter a task description: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process using match-case

match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is of HIGH priority"
    case "medium":
        reminder = f"Reminder: Your task '{task}' is of MEDIUM priority"
    case "low":
        reminder = f"Reminder: Your task '{task}' is of LOW priority"
    case _:
        # If user enters something unexpected
        reminder = f"Reminder: Your task '{task}' has UNKNOWN priority"

# Modify reminder based on time sensitivity

if time_bound == "yes":
    # time_bound and priority both matter
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Output the customized reminder

print(reminder)
