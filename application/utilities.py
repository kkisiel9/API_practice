
def get_time_of_day(time):
    if time < 12:
        return "Morning"
    elif time >= 12 and time < 16:
        return "Afternoon"
    elif time >= 16 and time < 19:
        return "Evening"
    else:
        return "Night"


