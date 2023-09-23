def seconds_since_midnight(hour, minute,second):
    hours_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    return hours_in_seconds + minute_in_seconds + second


seconds = seconds_since_midnight(13,30,45)
print(seconds)
