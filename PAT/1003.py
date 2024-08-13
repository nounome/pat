
citys,roads,start,end=map(int,input().split())

num_of_rescue=list(map(int,input().split()))

G=[[-1]*citys for _ in range(citys)]   #(起点，终点):长度

for i in range(roads):
    lu=list(map(int,input().split()))
    G[lu[0]][lu[1]]=lu[2]
    G[lu[1]][lu[0]]=lu[2]

visited=[]
unvisited=[i for i in range(citys)] 

d=[float('inf')]*citys  #表示起点到各地的距离
d[start]=0
pre=[-1]*citys

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

    for i in range(citys):
        if G[u][i]!=-1 and d[u]+G[u][i]<=d[i]:
            d[i]=d[u]+G[u][i]
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