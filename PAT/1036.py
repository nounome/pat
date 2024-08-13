
n=int(input())

mans=[]
womans=[]
for i in range(n):
    name,gender,idid,grade=input().split()
    if gender=='M':
        mans.append([name,idid,int(grade)])
    else:
        womans.append([name,idid,int(grade)])


if womans:
    womans.sort(key=lambda x:x[2],reverse=True)
    print(womans[0][0],womans[0][1])
else:
    print('Absent')
    
if mans:
    mans.sort(key=lambda x:x[2])
    print(mans[0][0],mans[0][1])
else:
    print('Absent')

if mans and womans:
    print(womans[0][2]-mans[0][2])
else:
    print('NA')