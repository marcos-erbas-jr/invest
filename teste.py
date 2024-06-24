
import datetime

data = "20/12/2024"

dt = data.split("/")
print(dt)

timestamp = datetime.datetime.timestamp(datetime.datetime(int(dt[2]), int(dt[1]), int(dt[0]), 23, 59, 59))
print(timestamp)