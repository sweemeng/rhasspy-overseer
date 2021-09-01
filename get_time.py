import datetime
from humanize.time import naturaltime


def say():
    now = datetime.datetime.now()
    return naturaltime(now.strftime("%H:%M"))
