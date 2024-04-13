DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, starting_day=None):
    start_time, start_period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if start_period == 'PM':
        start_hour += 12

    # Add duration to start time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Adjust minutes and hours
    new_hour += new_minute // 60
    new_minute %= 60

    # Calculate days passed and adjust new_hour for 12-hour format
    days_passed = new_hour // 24
    new_hour %= 24

    # Determine new period (AM/PM)
    new_period = 'AM' if new_hour < 12 else 'PM'

    # Adjust new_hour for 12-hour clock display
    new_hour = new_hour if 1 <= new_hour <= 12 else abs(new_hour - 12)

    # Format new_time string
    new_time = f'{new_hour}:{new_minute:02d} {new_period}'

    # Calculate and format the day of the week, if starting_day is provided
    if starting_day:
        day_index = (DAYS_OF_WEEK.index(starting_day.capitalize()) + days_passed) % 7
        new_day = DAYS_OF_WEEK[day_index]
        new_time += f', {new_day}'

    # Add information about the number of days passed
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time


print(add_time('3:00 PM', '3:10'), f"Expected: 6:10 PM")
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'), f"Expected: 2:02 PM, Monday")
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'), f"Expected: 12:03 PM")
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'), f"Expected: 1:40 AM (next day)")
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'), f"Expected: 12:03 AM, Thursday (2 days later)")
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'), f"Expected: 7:42 AM (9 days later)")
# Returns: 7:42 AM (9 days later)
