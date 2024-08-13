# 测试点2、4、5：如果有一个人开始服务时间在5点之前（不包括5点），
# 结束服务时间在5点之后，那么需要服务这个人


m,n,k,q=map(int,input().split())

cost=list(map(int,input().split()))
cost=[[i+1,x] for i,x in enumerate(cost)]   #【用户id，所需时间】

def dui_man(dui):   #判断队满
    for d in dui:
        if len(d)!=n:
            return False
    return True

def insert_dui(dui,yuansu):     #入队
    len_dui=[len(d) for d in dui]
    min_v=min(len_dui)

    index=[]
    for i,d in enumerate(dui):
        if len(d)==min_v:
            index.append(i)
    
    dui[index[0]].append(yuansu)

    return dui

def pop_dui(dui):
    global counttime
    head_time=[x[0][1] for x in dui if len(x)>0]
    minv=min(head_time)
    for i,d in enumerate(dui):
        if len(d)==0:continue
        dui[i][0]=[dui[i][0][0],dui[i][0][1]-minv]  

     
        if dui[i][0][1]==0:
            flag.append([dui[i][0][0],counttime+minv])
            del dui[i][0]

    return dui,minv

counttime=0
dui=[[] for _ in range(m)]
cur=0
flag=[]

un_rudui=[]
while cur<k and not dui_man(dui):
    while cur<k and not dui_man(dui):

        dui=insert_dui(dui,cost[cur])
        cur+=1

    dui,c_time=pop_dui(dui)   
    counttime+=c_time

while len(flag)<k:
    dui,c_time=pop_dui(dui)
    counttime+=c_time


map_flag={}
for i,j in flag:
    map_flag[i]=j

ask=list(map(int,input().split()))
for i in ask:
    res=map_flag[i]
    starttime=res-cost[i-1][1]   #计算服务开始时间！！！！！
    h=8+(res//60)
    m=res%60  

    if starttime>=60*(17-8):
        print('Sorry')

    else:
        if len(str(h))==1:
            h='0'+str(h)
        if len(str(m))==1:
            m='0'+str(m)
        print(('{}:{}').format(h,m))

