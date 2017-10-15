import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


def twitterapijob():
    subprocess.Popen(['C:\\python27\\python.exe', 'TwitterAPIcaller.py'])


scheduler= BlockingScheduler()
scheduler.add_job(twitterapijob,'interval',seconds=600)
scheduler.start()