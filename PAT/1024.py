
num,step=map(int,input().split())

cur_step=0

while str(num)!=str(num)[::-1] and cur_step<step:
    num=num+int(str(num)[::-1])
    cur_step+=1

print(num)
print(cur_step)
