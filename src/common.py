import datetime

def getCurrentTime():
    natural_date = datetime.datetime.now().strftime("%I %M %p")
    return natural_date.lstrip('0')
