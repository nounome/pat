

a,b=map(int,input().split())

res=a+b

if res>=0:
    fuhao=[]
else:
    fuhao=['-']
    res=-res

res=str(res)
count=0
ans=[]
for i in res[::-1]:
    if count==3:
        ans.append(',')
        ans.append(i)
        count=1
    else:
        ans.append(i)
        count+=1
ans=ans+fuhao

ans=ans[::-1]
print(('').join(ans))