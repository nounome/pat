#看1018dfs更简结代码


C_maxcapacity,N_numofstation,S_indexofproblem,M_numofroads=map(int,input().split())

current_bikes=list(map(int,input().split()))


G=[[-1]*(N_numofstation+1) for _ in range(N_numofstation+1)]


for i in range(M_numofroads):
    info=list(map(int,input().split()))   #一定是整数吗？
    G[info[0]][info[1]]=info[2]
    G[info[1]][info[0]]=info[2]

def dijiest(G,begin,targrt):
    d_current=[float('inf')]*(len(G))
    d_current[begin]=0

    visited=[]
    pre=[[] for _ in range(len(G))]   #有多条最短路径时前节点也可能有多个

    def select(d_current,visited):
        ind,val=-1,float('inf')
        for i in range(len(d_current)):
            if i not in visited:
                if d_current[i]<val:
                    val=d_current[i]
                    ind=i
        return ind
                
    while len(visited)<len(G):

        p=select(d_current,visited)

        visited.append(p)

        for q in range(len(G)):
            if q not in visited and G[p][q]!=-1 and d_current[p]+G[p][q]<=d_current[q]:
                pre[q].append(p)
                d_current[q]=d_current[p]+G[p][q]

    return d_current[targrt],pre

shortpath,pre=dijiest(G,0,S_indexofproblem)

def dfs(end):
    if end[-1]==0:
        lujings.append(end[:])
        return
    for i in (pre[end[-1]]):
        dfs(end+[i])

lujings=[]   #由于前节点有多个，此时的路径可能不是最短路径
dfs([S_indexofproblem])

res_lujings=[]
for lujing in lujings:
    lu=lujing[::-1]
    path=0
    for i in range(len(lu)-1):
        path+=G[lu[i]][lu[i+1]]

    if path==shortpath:    #筛选掉非最短路径
        res_lujings.append(lu)


res=[] 

for res_lujing in res_lujings:
    add,takeback=0,0      #模拟路径。记录需要sent和带回的车辆数
    cur_take=0           #记录到达某个站点时携带的车辆数

    for i in res_lujing[1:]:
        if current_bikes[i-1] > (C_maxcapacity//2):
            cur_take+=(current_bikes[i-1] - (C_maxcapacity//2))
        elif current_bikes[i-1] < (C_maxcapacity//2):
            if cur_take>=(C_maxcapacity//2)-current_bikes[i-1]:
                cur_take-=(C_maxcapacity//2)-current_bikes[i-1]
            else:
                add+=((C_maxcapacity//2)-current_bikes[i-1]) - cur_take
                cur_take=0
    if cur_take>0:
        takeback=cur_take

    res.append([add,res_lujing,takeback])

res.sort(key=lambda x:x[0])    #send相同时再考虑回收数，没写

lu_res=('->').join([str(x) for x in res[0][1]])
print(res[0][0],lu_res,res[0][2])