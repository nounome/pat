

from copy import deepcopy

# 定义深度优先搜索的函数
def dfs(start):
    global temp, best, problem_station_index, stations
    if temp[0] > best[0]:
        return
    if start == problem_station_index and (temp[0] < best[0] or (
            temp[0] == best[0] and (temp[1] < best[1] or (temp[1] == best[1] and temp[2] < best[2])))):
        best = temp
        return

    for i in stations[start][2]:
        to, time = i[0], i[1]
        if not stations[to][3] and stations[to][0] >= stations[start][0] + time:
            # 这个点的目前最佳时间比不上新路径的时间，那么需要考虑是否要更新
            stations[to][0] = stations[start][0] + time
            stations[to][3] = True
            back = deepcopy(temp)	# 记录当前状态，用深拷贝是因为temp最后一项是列表
            temp[0] += time
            temp[2] += stations[to][1]
            if temp[2] < 0:
                temp[1] -= temp[2]
                temp[2] = 0
            temp[3].append(to)
            dfs(to)		# 进入下一个车站
            stations[to][3] = False		# 回溯
            temp = deepcopy(back)

# 元数据读入
capacity, stations_num, problem_station_index, roads_num = list(map(int, input().split()))
bike_info = input().split()
# 生成车站列表
stations = [[0, 0, [], False]] + [[9999, int(i) - capacity // 2, [], False] for i in bike_info]
# 读入路和时间
for _ in range(roads_num):
    a = input().split()
    stations[int(a[0])][2].append((int(a[1]), int(a[2])))
    stations[int(a[1])][2].append((int(a[0]), int(a[2])))

best = [9999, 9999, 9999, []]
temp = [0, 0, 0, []]
# 深度优先搜索
dfs(0)
# 输出结果
print(best[1], end=' 0')
for i in best[3]:
    print("->" + str(i), end='')
print(" " + str(best[2]))