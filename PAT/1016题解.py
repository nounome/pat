
from collections import defaultdict

# 给定dd:hh::mm的字符串，返回从这个月头到这个时间点的总分钟数和总价格（假设每一分都在打电话）
def time_to_money(a: str):
    day, hour, minute = int(a[:2]), int(a[3:5]), int(a[6:])
    minutes = day * 24 * 60 + hour * 60 + minute
    money = sum(toll) * 60 * day
    for i in range(hour):
        money += toll[i] * 60
    money += toll[hour] * minute
    return minutes, money

# 数据结构初始化与录入数据
toll = list(map(int, input().split()))
records = defaultdict(list)
num_records = int(input())
for i in range(num_records):
    info = input().split()
    records[info[0]].append((info[1], info[2]))
    if i == 0: month = info[1][:2]

# 清理数据
for i in records.keys():
    records[i].sort(key=lambda x: x[0])
    temp_list = []
    for j, k in enumerate(records[i]):
        if j + 1 < len(records[i]) and k[1] == "on-line" and records[i][j + 1][1] == "off-line":
            temp_list.append((k[0][3:], records[i][j + 1][0][3:]))
    records[i] = temp_list

# 计算并输出
name_list = sorted([i for i in records.keys() if records[i]])
for user in name_list:
    print(user, month)
    sums = 0
    for begin, end in records[user]:
        minute_begin, money_begin = time_to_money(begin)
        minute_end, money_end = time_to_money(end)
        print("%s %s %d %c%.2f" % (begin, end, minute_end - minute_begin, "$", (money_end - money_begin) / 100))
        sums += (money_end - money_begin)
    print("Total amount: $%.2f" % (sums / 100))