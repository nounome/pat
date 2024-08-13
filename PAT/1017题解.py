
# 读取数据并初始化
num_cus, num_windows = list(map(int, input().split()))
arrive, process, pop = [], [], [28800 for _ in range(num_windows)]
total_wait = 0

information = []
for _ in range(num_cus):
    information.append(input().split())
information.sort(key=lambda x: x[0])

for a, pro_time in information:
    time = int(a[:2]) * 3600 + int(a[3:5]) * 60 + int(a[6:])
    if time > 61200:
        num_cus -= 1
        continue
    else:
        arrive.append(time)
    if int(pro_time) > 60:
        process.append(3600)
    else:
        process.append(int(pro_time) * 60)

# 模拟排队的流程
cus_id = 0
while cus_id < num_cus:
    window = pop.index(min(pop))
    if pop[window] - arrive[cus_id] > 0:
        total_wait += (pop[window] - arrive[cus_id])
        pop[window] += process[cus_id]
    else:
        pop[window] = arrive[cus_id] + process[cus_id]
    cus_id += 1

print("%.1f" % (total_wait / num_cus / 60))
