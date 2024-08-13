
import collections
n,k=map(int,input().split())

d=collections.defaultdict(list)

for i in range(k):
    index,Ni=map(int,input().split())
    students=input().split()
    for stu in students:
        d[stu].append(index)


        
all_student=input().split()
for stu in all_student:
    if len(d[stu])==0:
           print(stu,0)
    else:
        print(stu,len(d[stu]),end=' ')
        xuhao=sorted(d[stu])
        print((' ').join([str(x) for x in xuhao]))