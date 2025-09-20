# # Prompt user inputs exactly as expected by the tests

# task = input("Enter your task:")
# time_bound = input("Is it time-bound?(yes/no):")
# priority = input("Priority(high/medium/low):")

# # Process based on priority and time sensitivity

# match priority:
#     case "high":
#         reminder = f"Reminder: Your task '{task}' is of HIGH priority"
#     case "medium":
#         reminder = f"Reminder: Your task '{task}' is of MEDIUM priority"
#     case "low":
#         reminder = f"Reminder: Your task '{task}' is of LOW priority"
#     case _:
#         reminder = f"Reminder: Your task '{task}' has UNKNOWN priority"

# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# else:
#     reminder += "."

# print(reminder)
task = input("Enter your task:")
time_bound = input("Is it time-bound?(yes/no):")
priority = input("Priority(high/medium/low):")

match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is of HIGH priority"
    case "medium":
        reminder = f"Reminder: Your task '{task}' is of MEDIUM priority"
    case "low":
        reminder = f"Reminder: Your task '{task}' is of LOW priority"
    case _:
        reminder = f"Reminder: Your task '{task}' has UNKNOWN priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

print(reminder)
