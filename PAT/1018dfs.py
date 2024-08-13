#多条最短路径的优先级是先send出的数量最少，
#当send数量相同时，再比较带回的车辆数最少的路径。  ！！！一直卡在这里，没考虑这一步测试点7、8未通过！！！

C_maxcapacity,N_numofstation,S_indexofproblem,M_numofroads=map(int,input().split())

current_bikes=list(map(int,input().split()))

G=[[-1]*(N_numofstation+1) for _ in range(N_numofstation+1)]

for i in range(M_numofroads):
    info=list(map(int,input().split()))   #一定是整数吗？yes
    G[info[0]][info[1]]=info[2]
    G[info[1]][info[0]]=info[2]

def dfs(lis):
    global min_distance

    if lis[-1]==S_indexofproblem:
        distance=0
        for k in range(1,len(lis)):
            distance+=G[lis[k-1]][lis[k]]
        if distance<=min_distance:
            min_distance=distance
            min_lus.append(lis[:])
        return
    
    if len(lis)==N_numofstation+1:
        return
    
    for i in range(1,N_numofstation+1):
        if i not in lis and G[lis[-1]][i]!=-1:
            dfs(lis+[i])

min_lus=[]      #有多条最短路
min_distance=float('inf')
dfs([0])


res=[]   #对于每条最短路记录[send的数量，路径，回收的数量]  怎样得出的很关键，注意体会！！！！
for res_lujing in min_lus:
    add,takeback=0,0    #send的数量，回收的数量
    cur_take=0         #记录到达某个站点时携带的车辆数

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

res.sort(key=lambda x:x[0])  #按照send的数量由小到大排序

same_send_res=[]      #！！！ 没考虑这部分，一直卡着
for x in res:
    if x[0]==res[0][0]:
        same_send_res.append(x)
same_send_res.sort(key=lambda x:x[2])  #！！！send相同时按回收数量排序

lu_res=('->').join([str(x) for x in same_send_res[0][1]])
print(same_send_res[0][0],lu_res,same_send_res[0][2])