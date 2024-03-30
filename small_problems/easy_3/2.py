from datetime import timedelta

SECS_IN_MIN = 60
MINS_IN_DAY = 1440

def after_midnight(time_str: str):
    hrs, mins = [int(unit) for unit in time_str.split(":")]
    t = timedelta(hours=hrs, minutes=mins)
    minutes = int(t.seconds / SECS_IN_MIN) % MINS_IN_DAY
    return minutes

def before_midnight(time_str: str):
    minutes = (MINS_IN_DAY - after_midnight(time_str)) % MINS_IN_DAY
    return minutes


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True