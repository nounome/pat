
k=int(input())
nums=list(map(int,input().split()))

f=[0]*k
f[0]=nums[0]

for i in range(1,k):
    if f[i-1]<=0:
        f[i]=nums[i]
    else:
        f[i]=f[i-1]+nums[i]


index=[]     
maxnum=max(f)
for i,v in enumerate(f):
    if v==maxnum:
        index.append(i)



if maxnum<0:
    print(0,nums[0],nums[-1])
elif maxnum==0:               #（刚开始没考虑的时候会显示测试点5不通过）
    print(0,nums[index[0]],nums[index[0]])
else:
    fanwei=[]
    for index_i in index:
        flag=False          #标记找到最开始是否有f小于0
        for j in range(index_i,-1,-1):
            if f[j]<=0:       #考虑当最大和为0的情况这里写成<的话，会导致另一个测试点超时
                flag=True
                break
        start_index=j+1 if flag else 0
        fanwei.append([start_index,index_i])

    fanwei.sort(key=lambda x:x[0])

    print(maxnum,nums[fanwei[0][0]],nums[fanwei[0][1]])   #注意是第一个数字和最后一个数字的值，而不是索引

