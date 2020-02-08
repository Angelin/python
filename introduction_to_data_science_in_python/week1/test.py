from datetime import datetime, timedelta

int_time_for_now = datetime.now()
d = timedelta(days=4)
type(d)
time_after_4_yrs = int_time_for_now + d

print('time now: ', str(int_time_for_now))