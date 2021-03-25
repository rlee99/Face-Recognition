import pandas as pd


def copy_csv(filename):
    df = pd.read_csv(filename)
    df.to_csv('FinalAttendance.csv', mode='a')
    f = open(filename, "w+")
    f.close()


copy_csv('Attendance.csv')
