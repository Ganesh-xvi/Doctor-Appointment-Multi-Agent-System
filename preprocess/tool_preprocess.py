from datetime import datetime

def convert_to_am_pm(time_str):
    # Split the time string into hours and minutes
    time_str = str(time_str)
    hours, minutes = map(int, time_str.split(":"))

    # Determine AM or PM
    period = "AM" if hours < 12 else "PM"

    # Convert hours to 12-hour format
    hours = hours % 12 or 12

    # Format the output
    return f"{hours}:{minutes:02d} {period}"

def convert_datetime_format(dt_str):
    # Parse the input datetime string
    dt = datetime.strptime(dt_str, "%d-%m-%Y %H:%M")

    # Format the output as 'DD-MM-YYYY H.M' (removing leading zero from hour only)
    return dt.strftime("%d-%m-%Y %#H.%M")