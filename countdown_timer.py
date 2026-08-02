import time
hour = int(input("Enter the number of hours for the countdown: "))
minutes = int(input("Enter the number of minutes for the countdown: "))
seconds = int(input("Enter the number of seconds for the countdown: "))
while hour > 0 or minutes > 0 or seconds > 0:
    print(f"Countdown: {hour} hours, {minutes} minutes and {seconds} seconds remaining")
    time.sleep(1)
    seconds-=1
    if seconds<0:
        minutes-=1
        seconds=59
        if minutes<0:
            hour-=1
            minutes=59
            seconds=59
        if hour<0:
            break
print("Countdown finished!")