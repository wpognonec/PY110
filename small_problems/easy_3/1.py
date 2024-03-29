import time

# def time_of_day(minute_time: int):
#     minute_time = minute_time % 1440
#     if minute_time < 0:
#         minute_time += 1440
#     hours = minute_time // 60
#     minutes = minute_time % 60
#     return f"{hours:02d}:{minutes:02d}"

DAYS = ["Sunday", "Monday", "Tuesday", "Wesnesday", "Thursday", "Friday", "Saterday"]
MINUTES_IN_DAY = 1440
SECONDS_IN_MINUTE = 60
DAYS_IN_WEEK = 7

def time_of_day(delta_minutes: int):
    day_index = (delta_minutes // MINUTES_IN_DAY) % DAYS_IN_WEEK 
    day_minutes = delta_minutes % MINUTES_IN_DAY
    day = DAYS[day_index]
    time_obj = time.gmtime(day_minutes * SECONDS_IN_MINUTE)
    formatted_time = time.strftime("%H:%M", time_obj)
    print(f"{day} {formatted_time}")
    return f"{day} {formatted_time}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True