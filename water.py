import os 
import time
from datetime import datetime
os.system('say "Water reminder started"')
while True:
    now = datetime.now()
    begin_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if begin_time <= now <= end_time:
        os.system('say "Time to drink water"')
        time.sleep(3600)
    elif now > end_time:
        os.system('say "Work day ended. Reminders stopped."')
        break
    else:
        wait_seconds = int((begin_time - now).total_seconds())
        wait_minutes = wait_seconds // 60     
        os.system(f'say "The time is {wait_minutes} minutes away from starting."')
        os.system(f'say "Reminders will start in {wait_minutes} minutes"')
        time.sleep(wait_seconds)