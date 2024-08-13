#开始有一个测试点没通过，是因为没有考虑在排名相同的情况下要按照id顺序来输出

n=int(input())

lis=[[] for _ in range(n)]
testdot={}
local_rank={}

for i in range(n):
    k=int(input())
    for j in range(k):
        info=list(input().split())
        testdot[info[0]]=i+1
        lis[i].append([info[0],int(info[1])])
    lis[i].sort(key=lambda x:x[1],reverse=True)
    index=0
    currank=1
    while currank<=len(lis[i]):
        count=1
        local_rank[lis[i][index][0]]=currank
        index+=1
        while index<len(lis[i]) and  lis[i][index][1]==lis[i][index-1][1]:
            local_rank[lis[i][index][0]]=currank
            index+=1
            count+=1
        currank+=count

all_info=[]
for li in lis:
    for l in li:
        all_info.append([l[0],int(l[1])])
all_info.sort(key=lambda x:x[1],reverse=True)

all_rank={}
index=0
currank=1
while currank<=len(all_info):
    count=1
    all_rank[all_info[index][0]]=currank
    index+=1
    while index<len(all_info) and  all_info[index][1]==all_info[index-1][1]:
        all_rank[all_info[index][0]]=currank
        index+=1
        count+=1
    currank+=count


print(len(all_rank))
res_allrank=sorted(all_rank.items(),key=lambda x:(x[1],x[0]))   #注意这里先按排名顺序后按id顺序
for k,v in res_allrank:
    print(k,v,testdot[k],local_rank[k])
