import datetime

def timelog(log):
    now = datetime.datetime.now()
    print("[" + now.strftime("%H:%M:%S") + "]", log)