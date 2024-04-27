from datetime import datetime as dt

def friday_the_13ths(y: int):
    return [dt(y, m, 13).isoweekday() for m in range(1,13)].count(5)

friday_the_13ths(1986)      # 1
friday_the_13ths(2015)      # 3
friday_the_13ths(2017)      # 2
