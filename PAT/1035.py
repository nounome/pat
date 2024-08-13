
n=int(input())

res=[]
for i in range(n):
    user,password=input().split()
    modif=''
    flag=False
    for c in password:
        if c =='1':
            modif+='@'
            flag=True
        elif c=='0':
            modif+='%'
            flag=True
        elif c=='l':
            modif+='L'
            flag=True
        elif c=='O':
            modif+='o'
            flag=True
        else:
            modif+=c
    if flag:
        res.append([user,modif])

if res:
    print(len(res))
    for x in res:
        print((' ').join(x))
else:
    if n==1:
        print('There is 1 account and no account is modified')
    else:
        print(f'There are {n} accounts and no account is modified')