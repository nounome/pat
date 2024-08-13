#解法1：超时
start1,start2,n=input().split()

d={}

for i in range(int(n)):
    info=input().split()
    d[info[0]]=[info[1],info[2]]  #存储值和next的地址


#如果两个单词相同呢
path1=[start1]
while start1!='-1':
    
    start1=d[start1][1]
    path1.append(start1)

path2=[start2]
while start2!='-1':
    start2=d[start2][1]
    path2.append(start2)

path1=path1[::-1]
path2=path2[::-1]

m=min(len(path1),len(path2))
i=0

while i<m:
    if path1[i]==path2[i]:
        i+=1
    else:
        flag=1
        break

print(path1[i-1])



#解法二，用字典记录pre，有bug尚未解决
# start1,start2,n=input().split()

# d={}

# for i in range(int(n)):
#     info=input().split()
#     if info[2] not in d:
#         d[info[2]]=[(info[0],info[1])]  #存储值和pre的地址
#     else:
#         d[info[2]].append((info[0],info[1]))

# address='-1'
# while address!=start1 and address!=start2:
#     if len(d[address])>1:
#         break

#     address=d[address][0][0]

# print(address)