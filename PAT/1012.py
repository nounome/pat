
N,M=map(int,input().split())

id,c,m,e,ave={},[],[],[],[]
for i in range(N):
    lis=list(map(int,input().split()))
    id[lis[0]]=i
    c.append(lis[1])
    m.append(lis[2])
    e.append(lis[3])
    ave.append(round(sum(lis[1:])/3,2))


c_sort=sorted(c,reverse=True)
m_sort=sorted(m,reverse=True)
e_sort=sorted(e,reverse=True)
ave_sort=sorted(ave,reverse=True)

d={1:'C',2:'M',3:'E',0:'A'}

for i in range(M):
    id_i=int(input())
    if id_i not in id:
        print('N/A')
    else:
        index=id[id_i]
        res=[]            #记录四项的名次[ave,c,m,e]
        res.append(ave_sort.index(ave[index])+1)  #注意这里必须先添加ave，因为优先级最高
        res.append(c_sort.index(c[index])+1)
        res.append(m_sort.index(m[index])+1)
        res.append(e_sort.index(e[index])+1)


        rank=min(res)
        rank_index=res.index(rank)   #可能有几个并列的最优名次，这里取第一个，也就是优先级最高的一个

        print(rank,d[rank_index])