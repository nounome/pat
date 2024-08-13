#本题也卡了好久，注意模拟窗口的思路，重点复习


n,k=map(int,input().split())

records=[]

def to_sum_s(str_time):
    h,m,s=str_time[0:2],str_time[3:5],str_time[6:8]
    total_s=int(h)*60*60+int(m)*60+int(s)
    return total_s

for i in range(n):
    info=input().split()
    flag=int(info[1])
    if flag>=60:             ############ 最多服务60分钟
        flag=60

    if to_sum_s(info[0])<=to_sum_s('17:00:00'):   #到达时间超过17点的不服务，
        records.append([info[0],flag])            #但到达时间小于17点但服务开始时间大于17点的要服务 

records.sort(key=lambda x:x[0])

cur=0
count_time=0
use_count=len(records)   #有效客户数量，不包括到达时间超过17点的

#模拟排队
windows=[to_sum_s('08:00:00') for _ in range(k)]   #表示每个窗口结束服务的空闲时间
while cur<use_count:
    index=windows.index(min(windows))
    arrive_time=to_sum_s(records[cur][0])
    if arrive_time>windows[index]:
        windows[index]=arrive_time+records[cur][1]*60
    else:
        count_time += windows[index] - arrive_time
        windows[index]+=records[cur][1]*60
    cur+=1
        
if use_count==0:
    print(0)
else:
    print(('{:.1f}').format(count_time/use_count/60))