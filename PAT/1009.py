A=list(map(float,input().split()))
B=list(map(float,input().split()))

k=[0]*2005  #下标表示指数，值表示系数           一开始只开到1000+
            #测试点3、4一开始没通过，因为系数范围0-1000，因此相乘之后最大为2000，因为数字要开到2000+


for i in range(1,len(A),2):
    for j in range(1,len(B),2):
        A_zhishu,B_zhishu=A[i],B[j]
        A_xishu,B_xishu=A[i+1],B[j+1]
        k[int(A_zhishu+B_zhishu)]+=(A_xishu*B_xishu)


count=0
res=[]
for i,v in enumerate(k):
    if v!=0:
        count+=1
        res.append([i,round(v,1)])

res.sort(key=lambda x:x[0], reverse=True)

res=[str(x) for lis in res for x in lis]
res=[str(count)]+res
print((' ').join(res))