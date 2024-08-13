
n,m=map(int,input().split())

childs=[[] for _ in range(n+1)]   #记录树结构，下标对应数据为该节点的孩子节点

for i in range(m):
    info=list(map(int,input().split()))
    parent_id=info[0]
    k=info[1]
    child=info[2:]
    childs[parent_id]=child




#ceng=[[] for _ in range(n+2)]  #记录每一层的节点


res=[]
# index=2
ceng_nodes=[1]   #由这一层节点得到下一层节点
# ceng[1]=[1]
while ceng_nodes:
    count=0
    ceng_nodes_copy=[]
    for i in ceng_nodes:
        if childs[i]==[]:count+=1
        for j in childs[i]:
            ceng_nodes_copy.append(j)
    
    res.append(str(count))
    # ceng[index]=ceng_nodes_copy
    # index+=1
    ceng_nodes=ceng_nodes_copy

print((' '.join(res)))