
nums=input().split()

n=int(nums[0])
nums=nums[1:]

nums.sort()

res=['0']
same=[]
for c in nums:
    if not same:
        same.append(c)
    else:
        if c[0]==same[-1][0]:
            same.append(c)
        else:
            before_after=[]
            min_len=min([len(x) for x in same])   #测试点5：n=3 34 341 3413 
            for sa in same:
                sa_after=sa+sa[0:min_len]   #注意这一步的妙处，一位一位比较，如果无位了，将前缀依次填补再比较
                before_after.append([sa,sa_after])
            before_after.sort(key=lambda x:x[1])
            res.append(('').join([x[0] for x in before_after]))

            same=[c]

if same:
        before_after=[]
        min_len=min([len(x) for x in same])
        for sa in same:
            sa_after=sa+sa[0:min_len]
            before_after.append([sa,sa_after])
        before_after.sort(key=lambda x:x[1])
        res.append(('').join([x[0] for x in before_after]))

ans=('').join(res)

# x=[x for x in range(1000000)]   #用来在pat针对非零返回 测试是哪段代码报错

#测试点6 有点迷，在int(ans)时会报错，需要按以下写法把前置0消去，以下写法又需要额外判断 测试点2全是0的情况
# 猜想是数字太太太太太太大了，位数达到上万位直接int(ans)就报错了
index=0
for i in range(len(ans)):
    if ans[i]=='0':
        index+=1
    else:
        break
if ans[index:]:
    print(ans[index:])
else:
    print(0)       #测试点2