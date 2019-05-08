from datetime import datetime
from datetime import timedelta


start_date = datetime(1, 1, 1)

date = start_date + timedelta(days=10.5)

print(date)