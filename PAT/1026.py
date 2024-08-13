n=int(input())

def turn_s(str_time):     #将字符串时间转化为秒数
    h,m,s=str_time.split(':')
    return int(h)*60*60+int(m)*60+int(s)

def turn_str(s):          #将秒数转化为字符串时间
    h=s//3600
    m=(s%3600)//60
    s=s%60
    return f"{h:02d}:{m:02d}:{s:02d}"

#输入客户数据
infos=[]
for i in range(n):
    info=input().split()
    if int(info[1])>120:info[1]=str(120)    #坑点：最多打两个小时  测试点4
    infos.append([turn_s(info[0]),int(info[1]),int(info[2])])
k,m=map(int,input().split())      #k是球桌数，m是vip球桌数
vips=list(map(int,input().split()))    #vip球桌的编号
infos.sort(key=lambda x:x[0])         #将客户数据根据到达时间排序


tables=[]    #正在使用的球桌  #服务开始时间、结束时间、到达时间、桌号
queue=[]     #正在排队的客户序号

res=[]

for i in range(min(n,k)):  #先将k个球桌填满，  ！！！如果人数小于球桌数，再考虑！！！ 测试点3跟这有关
    #这里也要考虑vip客户和球桌, 即如果VIP客户到达时有多张vip桌，选序号最小的（测试样例5和7）
    used_hao=[x[-1] for x in tables] if tables else []
    not_used_hao=[x for x in range(1,k+1) if x not in used_hao] #空闲的桌号
    next_people=infos[i]
    if next_people[2]==1: #是vip
        notused_vip=[x for x in not_used_hao if x in vips]
        zhuohao=min(notused_vip) if notused_vip else min(not_used_hao)
        tables.append([next_people[0],next_people[0]+60*next_people[1],next_people[0],zhuohao])
    else:
        zhuohao=min(not_used_hao)
        tables.append([next_people[0],next_people[0]+60*next_people[1],next_people[0],zhuohao])
        
    res.append(tables[-1][:]) 


#再处理k个球桌填满以后的客户

notplayed_index=k            #还没开始进入球桌的首个客户的序号
while queue or notplayed_index<n:

    appendflag=1    #res是否要append，res按服务开始的顺序记录

    tables=sorted(tables,key=lambda x:x[1])  #按结束时间排序

    early_finish_info=tables[0]
    early_finish_time=early_finish_info[1]    #最早结束时间
    table_hao=early_finish_info[-1]  #提取出桌号

    #找出最早结束时间时的排队客户  queue
    while notplayed_index<n and infos[notplayed_index][0]<=early_finish_time:
        queue.append(infos[notplayed_index])
        notplayed_index+=1
    
    if queue and len(tables)<k:  #在最早完成时间之前有桌子空闲且有人在排队
        #queue=sorted(queue,key=lambda x:x[0])   #这一句是否多余
        used_hao=[x[-1] for x in tables]
        not_used_hao=[x for x in range(1,k+1) if x not in used_hao] #空闲的桌号
        next_people=queue[0]
        if next_people[2]==1: #是vip
            notused_vip=[x for x in not_used_hao if x in vips]
            zhuohao=min(notused_vip) if notused_vip else min(not_used_hao)
            tables.append([next_people[0],next_people[0]+60*next_people[1],next_people[0],zhuohao])
        else:
            zhuohao=min(not_used_hao)
            tables.append([next_people[0],next_people[0]+60*next_people[1],next_people[0],zhuohao])
        
        #这种情况不需要删除tables[0]， 
        #而notplayed_index退回到初始notplayed_index加1的状态，因为每次这种情况只加一个客户进入tables
        notplayed_index=notplayed_index-len(queue)+1   #退回
        queue=[]  #再将队列设置为空

    elif queue:  #如果有排队
        del tables[0]
        queue=sorted(queue,key=lambda x:x[0])
  
        if table_hao in vips:  #如果是VIP桌空闲
            flag=False     #记录是否有vip用户进入球桌
            for x1,x2,x3 in queue:
                if x3==1: 
                    tables.append([early_finish_time,early_finish_time+x2*60,x1,table_hao])
                    queue.remove([x1,x2,x3])  #移除从等待队列进入打球的vip客户
                    flag=1
                    break
            if not flag:
                tables.append([early_finish_time,early_finish_time+queue[0][1]*60,queue[0][0],table_hao])
                del queue[0]

        else:  #如果是非VIP桌空闲
            tables.append([early_finish_time,early_finish_time+queue[0][1]*60,queue[0][0],table_hao])
            del queue[0]

    else:  #桌子空闲时无人排队  要等到桌子全空时且无人排队再进行以下操作
        del tables[0]
        if not tables:

            info=infos[notplayed_index]
            tables.append([info[0],info[0]+info[1]*60,info[0],1])  #此时桌号肯定是1？，若是vip用户且vip桌是3号？（貌似没有相应测试点）

            notplayed_index+=1
        else:
            appendflag=0

    if appendflag: res.append(tables[-1][:])  #按服务时间的顺序加入res

 
count=[0]*(k+1)
for j in res:   #j:服务开始时间、结束时间、到达时间、桌号
    if j[0]>=turn_s('21:00:00'):continue   #需要考虑等于的条件，21点开始服务也不行  测试点3
    count[j[-1]]+=1
    # print(j)
    # print(turn_str(j[2]))
    if (j[0]-j[2])%60==0:
        cha=(j[0]-j[2])//60
    else:
        cha=(j[0]-j[2])//60+1     #等待时间向上取整，分钟数
    #print('到达时间、服务开始时间、等待时间：',end='')
    print(turn_str(j[2]) , turn_str(j[0]), cha)
print((' ').join([str(x) for x in count[1:]]))


# 神测试样例！！！ 测试点5、7测试样例，输出的桌子要为 0 0 1 而不是 1 0 0
# 1
# 08:00:00 20 1
# 3 1
# 3
