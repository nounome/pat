#本题一直卡着，搞了好久，注意思路。计算花费时用前缀和思想，从本月一月一日到电话开始时间用的话费减去
# 从本月一月一日到电话结束时间用的话费

cost_perhour=list(map(int,input().split()))

n=int(input())
name=[]
record=[[] for i in range(n)]
res=[[] for i in range(n)]

for i in range(n):
    jilu=input().split()
    if jilu[0] not in name:
        name.append(jilu[0])
    index=name.index(jilu[0])
    record[index].append(jilu[1:])

for i,record_i in enumerate(record):
    if record_i==[]: continue
    record_i.sort(key=lambda x:x[0])
    for haoma,time_record in enumerate(record_i[:-1]):
        if time_record[1]=='on-line' and record_i[haoma+1][1]=='off-line':
            res[i].append([time_record[0],record_i[haoma+1][0]])


map_res={}
for i in range(len(name)):
    map_res[name[i]]=res[i]


sorted_map=sorted(map_res.items(),key=lambda x:x[0])


def culcost(timelist):
    cost=0
    total_min=0

    timeli=timelist

    start_day=int(timeli[0][3:5])
    end_day=int(timeli[1][3:5])

    start=timeli[0][6:]
    end=timeli[1][6:]

    if start_day==end_day:

        start_hour=int(start[:2])
        start_min=int(start[-2:])
        end_hour=int(end[:2])
        end_min=int(end[-2:])

        for i in range(start_hour,end_hour+1):
            if start_hour==end_hour:
                cost+=(end_min-start_min)*(cost_perhour[i]*0.01)
                total_min+=(end_min-start_min)
            elif i==start_hour:
                cost+=(60-start_min)*(cost_perhour[i]*0.01)
                total_min+=(60-start_min)
            elif i==end_hour:
                cost+=(end_min)*(cost_perhour[i]*0.01)
                total_min+=(end_min)
            else:
                cost+=60*(cost_perhour[i]*0.01)
                total_min+=60

    else:
        for day in range(start_day,end_day+1):
            if day==start_day:
                start_hour=int(start[:2])
                start_min=int(start[-2:])
                end_hour=23
                end_min=60
                for i in range(start_hour,end_hour+1):
                    if start_hour==end_hour:
                        cost+=(end_min-start_min)*(cost_perhour[i]*0.01)
                        total_min+=(end_min-start_min)
                    elif i==start_hour:
                        cost+=(60-start_min)*(cost_perhour[i]*0.01)
                        total_min+=(60-start_min)
                    elif i==end_hour:
                        cost+=(end_min)*(cost_perhour[i]*0.01)
                        total_min+=(end_min)
                    else:
                        cost+=60*(cost_perhour[i]*0.01)
                        total_min+=60
            elif day==end_day:
                start_hour=0
                start_min=0
                end_hour=int(end[:2])
                end_min=int(end[-2:])
                for i in range(start_hour,end_hour+1):
                    if start_hour==end_hour:
                        cost+=(end_min-start_min)*(cost_perhour[i]*0.01)
                        total_min+=(end_min-start_min)
                    elif i==start_hour:
                        cost+=(60-start_min)*(cost_perhour[i]*0.01)
                        total_min+=(60-start_min)
                    elif i==end_hour:
                        cost+=(end_min)*(cost_perhour[i]*0.01)
                        total_min+=(end_min)
                    else:
                        cost+=60*(cost_perhour[i]*0.01) 
                        total_min+=60
            else:
                start_hour,start_min=0,0
                end_hour,end_min=23,60
                for i in range(start_hour,end_hour+1):
                    if i==start_hour:
                        cost+=(60-start_min)*(cost_perhour[i]*0.01)
                        total_min+=(60-start_min)
                    elif i==end_hour:
                        cost+=(end_min)*(cost_perhour[i]*0.01)
                        total_min+=(end_min)
                    else:
                        cost+=60*(cost_perhour[i]*0.01) 
                        total_min+=60

    return total_min,"{:.2f}".format(cost)


for value in sorted_map:
    if value[1]==[]:
        continue
    print(value[0],value[1][0][0][:2])
    totalamount=0

    for time in value[1]:
        sb1,sb2=time[0][3:],time[1][3:]  #注意不需要打印月份！！！一直卡在这里一分没得！！！！！！！！
        print(sb1,sb2,end=' ')
        A,B=culcost(time)
        totalamount+=float(B)
        print('{} ${}'.format(str(A),str(B)))


    print('Total amount: ${:.2f}'.format(totalamount))
