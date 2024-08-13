
n,m,s,d=map(int,input().split())  #城市数、道路数、起点、终点

#路是单项还是双向的？    双向的，测试点1、2跟这个有关
roads={}
Distance_Cost={}
for i in range(m):
    info=list(map(int,input().split()))
    if info[0] not in roads:
        roads[info[0]]=[info[1]]
    else:
        roads[info[0]].append(info[1])

    if info[1] not in roads:
        roads[info[1]]=[info[0]]
    else:
        roads[info[1]].append(info[0])

    Distance_Cost[(info[0],info[1])]=(info[2],info[3])
    Distance_Cost[(info[1],info[0])]=(info[2],info[3])

def dfs(paths,val_dist,val_cost):
    if paths[-1]==d:
        res.append(paths[:]+[val_dist,val_cost])
        return

    for nextnode in roads[paths[-1]]:
        if nextnode not in paths:
            dfs(paths+[nextnode], val_dist+Distance_Cost[(paths[-1],nextnode)][0], val_cost+Distance_Cost[(paths[-1],nextnode)][1])


res=[]
dfs([s],0,0)

res.sort(key=lambda x:(x[-2],x[-1]))  #按路径和费用排序
print((' ').join(list(map(str,res[0]))))