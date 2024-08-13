citys,roads,start,end=map(int,input().split())

num_of_rescue=list(map(int,input().split()))

G=[[] for _ in range(citys)]   #直接用邻接矩阵也能过，但这样用时更少  G[i]与城市i有路径的城市序号
G_map={}                     #G_map存储每两个城市之间的路长

for i in range(roads):
    lu=list(map(int,input().split()))
    G[lu[0]].append(lu[1])
    G[lu[1]].append(lu[0])
    G_map[(lu[0],lu[1])]=lu[2]
    G_map[(lu[1],lu[0])]=lu[2]

visited=[]
unvisited=[i for i in range(citys)]      #加这个防止超时！！！！！最重要一步

d=[float('inf')]*citys  #表示起点到各地的距离
d[start]=0

pre=[[] for _ in range(citys)]

def select_unvisited_min():
    min_d=float('inf')
    index=-1

    for i in unvisited:
        if d[i]<min_d:
            min_d=d[i]
            index=i

    return index


while len(visited)<citys:
    u=select_unvisited_min()

    for i in G[u]:
        if d[u]+G_map[(u,i)]<=d[i]:
            d[i]=d[u]+G_map[(u,i)]
            pre[i].append(u)

    visited.append(u)
    unvisited.remove(u)


lujing=[]
def dfs(end):
    if end[-1]==start:
        lujing.append(end[:])
        return
    
    for i in pre[end[-1]]:
        dfs(end+[i])
    
dfs([end])

countlist=[]
for lujing_i in lujing:
    count=0
    for i in lujing_i:
        count+=num_of_rescue[i]
    countlist.append(count)

print(len(lujing),end=' ')
print(max(countlist))