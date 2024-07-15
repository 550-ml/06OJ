def judge_acc(year, month, day):
    if year <= 0 or month < 1 or month > 12:
        return False
    # 简化天数判断逻辑
    if month == 2:
        return day <= 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else day <= 28
    return day <= 31

def calculate_day(year, month, day):
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_day[1] = 29
    ans = sum(month_day[:month - 1])
    ans += day
    return ans
    
while True:
    try:
        year, month, day = input().split(' ')
        year = int(year)
        month = int(month)
        day= int(day)
        # 判断合理性
        if not judge_acc(year, month, day):
            print('Input error!')
        else:
            print(calculate_day(year, month, day))
    except:
        break