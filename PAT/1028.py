
n,c=map(int,input().split())

infos=[]
for i in range(n):
    inp=(input().split())
    inp[2]=int(inp[2])     #注意要将成绩转化成整形再排序，否则字符型会出错，‘61’排在‘9’前面
    infos.append(inp)

if c==1:
    infos.sort(key= lambda x:x[0])
elif c==2:
    infos.sort(key= lambda x:(x[1],x[0]))
elif c==3:
    infos.sort(key= lambda x:(x[2],x[0]))

for info in infos:
    info[2]=str(info[2])
    print((' ').join(info))