

def turn13(num):   #将十进制数字转化为13进制
    if num==0:return  '0'  #注意特判0 测试点4
    chushu=13
    res=[]
    while num:
        yushu=num%chushu
        if yushu==10:
            res.append('A')
        elif yushu==11:
            res.append('B')
        elif yushu==12:
            res.append('C')
        else:
            res.append(str(yushu))
        num=num//chushu
    return (('').join(res[::-1]))

nums=list(map(int,input().split()))

res=['#']
for num in nums:
    res_i=turn13(num)
    if len(res_i)<2:
        res_i='0'+res_i
    res.append(res_i)

print(('').join(res))