
y1=list(map(float,input().split()))
y2=list(map(float,input().split()))

d={}
for i in range(1,len(y1),2):
    if y1[i] not in d:
        d[y1[i]]=y1[i+1]
    else:
        d[y1[i]]+=y1[i+1]

for i in range(1,len(y2),2):
    if y2[i] not in d:
        d[y2[i]]=y2[i+1]
    else:
        d[y2[i]]+=y2[i+1]


data=[]

for key,value in d.items():
    if value!=0:             #除去系数为0的项
        data.append([key,value])

k=len(data)   #k表示多项式的项数，需要除去系数为0的项

if not data:
    print(0)
else:

    data.sort(key=lambda x:x[0],reverse=True)

    res=[k]

    for lis in data:
        res.append(int(lis[0]))
        res.append(round(lis[1],1))   #保留一位小数，这个测试点一直没想到

    res=[str(i) for i in res]

    print((' ').join(res))


