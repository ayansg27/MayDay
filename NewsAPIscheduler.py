import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


def newsapijob():
    subprocess.Popen(['C:\\python27\\python.exe', 'newsapi.py'])


scheduler= BlockingScheduler()
scheduler.add_job(newsapijob,'interval',seconds=10)
scheduler.start()