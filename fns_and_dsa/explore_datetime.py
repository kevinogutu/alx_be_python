#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)

def calculate_future_date(days_to_add: int) -> datetime:
    now = datetime.now()
    delta = timedelta(days=days_to_add)
    future = now + delta
    return future

def main():
    display_current_datetime()

    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        if not user_input:
            print("You didn’t enter anything. Please try again.")
            continue
        try:
            days = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer (e.g. 10 or -5).")
            continue
        
        # Use the name future_date here
        future_date = calculate_future_date(days)
        # Call .strftime on future_date
        future_str = future_date.strftime("%Y-%m-%d")
        print("Future date:", future_str)
        break

if __name__ == "__main__":
    main()
