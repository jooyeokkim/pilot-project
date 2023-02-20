import time


def get_timelist(self):
    timelist = []
    now = time.localtime(time.time())
    now_year = now.tm_year
    now_mon = now.tm_mon
    for i in range(-6, 7):
        if now_mon + i < 1:
            timelist.append([now_year - 1, now_mon + i + 12])
        elif now_mon + i > 12:
            timelist.append([now_year + 1, now_mon + i - 12])
        else:
            timelist.append([now_year, now_mon + i])
    return {'timelist': timelist}