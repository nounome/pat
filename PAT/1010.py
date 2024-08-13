#首先，这题要找的进制可能很大，如果按顺序查找会超时。但题目中说结果不唯一时，取最小进制，这误导了我没去想二分
#用二分，左边界是目标数的各个位数的数的最大值+1，右边界是比较数的值+1，而且注意当位数是字母时注意映射

N1,N2,tag,radix=input().split()

def to_jinzhi(num,jinzhi):  #这里num是字符串
    res=0
    wei=1
    for i in num[::-1]:
        if i.isdigit():
            res+=int(i)*wei
            wei*=jinzhi
        else:
            i=10+ord(i)-ord('a')
            res+=i*wei
            wei*=jinzhi
    return res


if tag=='1':
    std_num=to_jinzhi(N1,int(radix))
    target_num=N2
else:
    std_num=to_jinzhi(N2,int(radix))
    target_num=N1

flag=False


def map_num(str_num):
    if str_num.isdigit():
        return int(str_num)
    else:
        return 10+ord(str_num)-ord('a')

low=max([map_num(x) for x in target_num])+1    #注意这里x可能是字母,要建立map映射
high=max(low,int(std_num))+1    #这里不加1也行

while low<=high:
    mid=(low+high)//2
    nownum=to_jinzhi(target_num,mid)
    if nownum==std_num:
        print(mid)
        flag=True
        break
    elif nownum<std_num:
        low=mid+1
    else:
        high=mid-1

if not flag:
    print('Impossible')

