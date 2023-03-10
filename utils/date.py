import time


def get_month_list():
    month_list = []
    now = time.localtime(time.time())
    now_year = now.tm_year
    now_mon = now.tm_mon
    for i in range(-6, 7):
        if now_mon + i < 1:
            month_list.append([now_year - 1, now_mon + i + 12])
        elif now_mon + i > 12:
            month_list.append([now_year + 1, now_mon + i - 12])
        else:
            month_list.append([now_year, now_mon + i])
    return month_list