import time
import winsound
import pandas as pd


def csv_to_sound(file_name="csv/beeps.csv"):
    data = pd.read_csv(file_name)
    for row in data.itertuples():
        # print(row)
        winsound.Beep(row[1], row[2])


def dial_up(nr=11263):
    for i in [int(x) for x in str(nr)]:
        winsound.PlaySound("sounds/Dtmf" + str(i) + ".wav", winsound.SND_FILENAME)


def request_sound():
    freq, duration = 0, 0
    while int(freq := input("Frequency: ")) in range(0, 32000) \
            and int(duration := input("Duration (ms): ")) in range(0, 5000):
        winsound.Beep(int(freq), int(duration))
    print(f"Bad value, f {freq} d {duration}")


def interval_reminder(duration=60, interval=10):
    """Beep reminder at an interval

    interval and duration in minutes"""

    for i in range(0, int(duration / interval)):
        print(f"Started {60 * interval}m interval")
        time.sleep(60 * interval)
        print("Reminder played...")
        reminder_sound()


def reminder_sound():
    for j in range(1, 6):
        winsound.Beep(2000 + j * 300, 50)


if __name__ == '__main__':
    # winsound.PlaySound("*", winsound.SND_ALIAS)

    # csv_to_sound()
    # dial_up(input("Type your phone number: "))
    # request_sound()
    interval_reminder()
