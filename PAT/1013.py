#最后一个测试点超时，python无解


N,M,K=map(int,input().split())

roads=[[0]*N for _ in range(N)]
edge=[]

for i in range(M):
    p,q=map(int,input().split())
    roads[p-1][q-1]=1
    roads[q-1][p-1]=1
    edge.append([p-1,q-1])

check=list(map(int,input().split()))

def find(x):
    while pre[x]!=x:
        x=pre[x]
    return pre[x]

for check_city in check:
    check_city-=1
    pre=[x for x in range(N)]
    count=N-2           #一开始想象各个点都没有连接路径，则N-1个点需要N-2条路

    for lis in edge:
        node1,node2=lis[0],lis[1]
        if node1==check_city or node2==check_city:
            continue
        root1,root2=find(node1),find(node2)
        if root1!=root2:    #说明这两点初始想象时没有联通，但实际上已修路，则需要修的路数-1
            count-=1
            pre[node1]=node2

    print(count)










    # nearby=[]
    # for i in range(N):
    #     if roads[check_city-1][i]==1:
    #         nearby.append(i)
    
    # if len(nearby)==1:
    #     print(0)
    # else:
    #     count=len(nearby)-1   #最大要修的条数，如果与check_city相连的城市有3个，且3个之间互不链接，则需要修3-1条
    #     dict={}
    #     for p in range(len(nearby)-1):
    #         for q in range(p+1,len(nearby)):
    #             if roads[nearby[p]][nearby[q]]==1 and nearby[q] not in dict:   #注意是nearby[p] 而不是p
    #                 count-=1         #一旦与check_city相连的城市互通，则需要修的条数减去1
    #                 dict[nearby[q]]=1

    #     count=count if count>=0 else 0
    #     print(count)
    