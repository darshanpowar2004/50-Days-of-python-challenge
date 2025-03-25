# Day 42
# Alarm Clock
import datetime
import winsound


def alarm():
    hours = input("Enter hour: ")
    minute = input("Enter minute: ")


    if int(hours) > 12 and int(minute) > 60:
        print("Invalid time. Try agin!")

    alarm_time = hours + ":" + minute

    print(f"Alarm set at {alarm_time}")

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if alarm_time == now:
            print("Weak Up !")
            print("Weak Up !")
            print("Weak Up !")
            winsound.PlaySound("digital-alarm-2-151919.wav",winsound.SND_FILENAME)

if __name__ == '__main__':
    alarm()