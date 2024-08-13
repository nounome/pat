
# 数据结构初始化与信息读入
num_nodes = int(input())
roads = [[] for _ in range(num_nodes + 1)]
for _ in range(num_nodes - 1):
    info = list(map(int, input().split()))
    roads[info[0]].append(info[1])
    roads[info[1]].append(info[0])
visited = [False for i in range(num_nodes + 1)]
maxheight = 0
max_nodes = []

# 深度优先遍历
def dfs(node, height):
    global maxheight
    if height > maxheight:
        max_nodes.clear()
        max_nodes.append(node)
        maxheight = height
    elif height == maxheight:
        max_nodes.append(node)
    visited[node] = True
    for i in roads[node]:
        if not visited[i]:
            dfs(i, height + 1)
            
# 计算连通分量,第一轮DFS
count = 0
for i in range(1, num_nodes + 1):
    if not visited[i]:
        dfs(i, 1)
        count += 1

# 输出与进行第二次DFS
if count >= 2:
    print("Error: %d components" % count)
else:
    ans = set(max_nodes)
    maxheight = 0
    visited = [False for _ in range(num_nodes + 1)]
    dfs(max_nodes[0], 1)
    ans = ans | set(max_nodes)
    ans = sorted(ans)
    for i in ans:
        print(i)
