import datetime
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def hourlyjob():
    print('running hourly job')


def secondjob():
    print('This job is run every 10 seconds.')


scheduler= BlockingScheduler()
scheduler.add_job(hourlyjob,'interval',hours=1)
scheduler.add_job(secondjob,'interval',seconds=10)
scheduler.start()