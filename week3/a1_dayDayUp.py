# 3.1 DayDayUp
def dayDayUp(workDayUp):
    count = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            count = count * (1 - 0.01)
        else:
            count = count * (1 + workDayUp)
    return count

workDayUpFactor = 0.01

while dayDayUp(workDayUpFactor) < 37.78:
    workDayUpFactor += 0.0001
print("工作日需要努力：{:.4f}".format(workDayUpFactor))
