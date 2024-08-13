
n=int(input())

G=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=input().split()
    G[int(a)]+=[int(b)]
    G[int(b)]+=[int(a)]
    
def cengxu(index):  #层序遍历算长度
    chang=0
    components=0

    shunxu=[index]+[x for x in range(1,n+1) if x!=index]
    for k in shunxu:
        if visited[k]==1:continue

        ceng=[k]
        while ceng:
            for c in ceng:
                visited[c]=1

            cengcopy=[x for c in ceng for x in G[c] if visited[x]==0]
            last_ceng=ceng
            ceng=cengcopy
            chang+=1

        if all(value == 1 for value in visited[1:]):
            break
        else:
            components+=1
        
    return components,last_ceng  #last_ceng记录叶子节点集合



#第一次随机选择起点，找出叶子结点集合
visited=[0]*(n+1)
components1,last_ceng1=cengxu(1)

if components1!=0:
    print('Error: {} components'.format(components1+1))   #注意要加1，components>=1表示不联通,不联通至少有两个区域
else:
    #第二次，叶子结点集合中随机选一点，找出其的叶子结点，答案为两叶子节点并集，妙！
    visited=[0]*(n+1)
    components2,last_ceng2=cengxu(last_ceng1[0])

    ans=last_ceng1 #好奇怪:用ans=set(last_ceng1)|set(last_ceng2) 过不了
    for c in last_ceng2:
        if c not in ans:
            ans.append(c)
    ans.sort()
    for i in ans:
        print(i)
