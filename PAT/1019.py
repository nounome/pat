#注意循环策略，每次除以b，商成为新的被除数，直到为0
N,b=map(int,input().split())

shang=N
res=[]
while True:
    shang,yushu = shang // b , shang % b
    res.append(yushu)
    if shang<=0:break


k=len(res)
flag=True
for i in range(0,k//2):    #回文判断可以直接res==res[::-1]
    if res[i]!=res[k-i-1]:
        flag=False
        break
if flag:
    print('Yes')
else:
    print('No')
print((' ').join([str(x) for x in res[::-1]]))
