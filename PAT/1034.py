#bfs和dfs都可以通过

import collections

n,k=map(int,input().split())

d=collections.defaultdict(list)

d2=collections.defaultdict(list)  #记录从name1为起点的

people=set()
for i in range(n):
    name1,name2,time=input().split()
    time=int(time)
    d[name1].append([name2,time])
    d[name2].append([name1,time])

    d2[name1].append([name2,time])
    people.add(name1)
    people.add(name2)


def bfs(names):
    res=[]
    queue=[names]
    visited.add(names)
    while queue:
        pp=queue.pop(0)
        res.append(pp)
        nextnames=[x[0] for x in d[pp]]
        nextnames=list(set(nextnames))
        
        for next in nextnames:
            if next not in visited:
                queue.append(next)
                visited.add(next)
    return res
                
def dfs(names):

    nextnames=[x[0] for x in d[names]]
    nextnames=list(set(nextnames))

    for next in nextnames:
        if next not in visited:
            res_i.append(next)
            visited.add(next)
            dfs(next)

    
visited=set()
cluster=[]
people=list(people)

for p in people:
    if p in visited: continue
    # res_i=bfs(p)

    res_i=[p]
    visited.add(p)
    dfs(p)
    cluster.append(res_i)


ans=[]
for gang in cluster:
    if len(gang)<=2: continue
    res=[]
    cluster_value=0
    for duiyuan in gang:
        value=sum([x[1] for x in d[duiyuan]])
        res.append([duiyuan,value])

        if duiyuan in d2:
            cluster_value+=sum([x[1] for x in d2[duiyuan]])

    if cluster_value<=k:continue

    res.sort(key=lambda x:x[1],reverse=True)
    ans.append((res[0][0],str(len(gang))))
if ans:
    ans.sort(key=lambda x:x[0])
    print(len(ans))
    for an in ans:
        print((' ').join(an))
else:
    print(0)