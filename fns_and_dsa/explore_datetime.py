#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    """Gets the current date and time, formats it, and prints it."""
    now = datetime.now()
    # Save date/time into variable (for clarity)
    current_date = now
    # Format as “YYYY-MM-DD HH:MM:SS”
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)

def calculate_future_date(days_to_add: int):
    """Given a number of days, returns a datetime.date (or datetime) for that future date."""
    now = datetime.now()
    # Create a timedelta representing the duration to add
    delta = timedelta(days=days_to_add)
    future_datetime = now + delta
    # We only need the date portion (you could also show time, depending on requirement)
    future_date = future_datetime.date()
    return future_date

def main():
    # Part 1
    display_current_datetime()

    # Part 2: ask user how many days to add
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        if not user_input:
            print("You didn't enter anything. Please try again.")
            continue
        # Try to convert to integer
        try:
            days = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer number of days (e.g. 10 or -5).")
            continue
        
        future = calculate_future_date(days)
        print("Future date:", future.strftime("%Y-%m-%d"))
        break

if __name__ == "__main__":
    main()
