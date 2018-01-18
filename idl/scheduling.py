#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗



from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

from jsontodb import *


def tick():
    for i in range(19,-1,-1):
        data = dataalljson['reviews'][i]
        savadb(data)

# 每隔600秒执行一次
# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#     scheduler.add_job(tick, 'cron', minute='*/5')
#     print 'Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C')
#     try:
#         scheduler.start()
#     except KeyboardInterrupt, SystemExit:
#         scheduler.shutdown()




# sched = BlockingScheduler()
#
# sched.add_job(tick,'cron',minute='*/5',id='tick')
# sched.start()
#
