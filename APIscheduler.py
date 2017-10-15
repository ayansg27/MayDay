import subprocess
import os
from apscheduler.schedulers.background import BackgroundScheduler


def twitterapijob():
    subprocess.call(['C:\\python27\\python.exe', 'C:\\Users\\ayans\\PycharmProjects\\MaydayWeb\\TwitterAPIcaller.py'])

def newsapijob():
    subprocess.call(['C:\\python27\\python.exe', 'C:\\Users\\ayans\\PycharmProjects\\MaydayWeb\\newsapi.py'])


scheduler= BackgroundScheduler()
scheduler.add_job(twitterapijob,'interval',seconds=15)
print os.getcwd()
scheduler.add_job(newsapijob,'interval',seconds=10)
scheduler.start()