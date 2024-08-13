# 1、题意难理解，比较绕
# 2、一开始测试点1没通过是判断素数时没有考虑周全

def tentoi(num,ijinzhi):
    res=[]
    while num>0:
        res.append(str(num%ijinzhi))
        num=num//ijinzhi

    return ('').join(res)
        
def panduansushu(num):
    if num==1:            #注意判断1不是素数！！！！！
        return False
    
    if num==2:
        return True     #注意2也要特判
    
    right=min(num-1,int(num**0.5+5)) #注意右边界取较小值
    for i in range(2,right+1):
        if num%i==0:
            return False
    return True

while True:
    data=list(map(int,input().split()))
    if data[0]<0:break
    num,jinzhi=data
    if not panduansushu(num):
        print('No')
        continue
        

    num_i=tentoi(num,jinzhi)
    if panduansushu(int(num_i,jinzhi)):
        print('Yes')
    else:
        print('No')