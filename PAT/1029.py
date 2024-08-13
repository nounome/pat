##解法1：常规暴力  竟然ac了
# nums=[]
# for i in range(2):
#     lis=list(map(int,input().split()))
#     for num in lis[1:]:
#         nums.append(num)
# nums.sort()

# if len(nums)%2==0:
#     print(nums[len(nums)//2-1])
# else:
#     print(nums[len(nums)//2])


#解法2：双指针找m+n中间数  超时

info1=list(map(int,input().split()))
m=info1[0]
nums1=info1[1:]

info2=list(map(int,input().split()))
n=info2[0]
nums2=info2[1:]

i,j=0,0
count=0

flag=False
while  i<m and j<n:
    if nums1[i]<nums2[j]:
        i+=1
        count+=1
        if (count>((m+n)//2) and (m+n)%2==1) or (count>=((m+n)//2) and (m+n)%2==0):
            print(nums1[i-1]) 
            flag=True
            break
    else:
        j+=1
        count+=1
        if (count>((m+n)//2) and (m+n)%2==1) or (count>=((m+n)//2) and (m+n)%2==0):
            print(nums2[j-1])
            flag=True
            break

if not flag: #要加这一句，因为可能i==m时，上面也输出了
    if i>=m:
        while True:
            j+=1
            count+=1
            if (count>((m+n)//2) and (m+n)%2==1) or (count>=((m+n)//2) and (m+n)%2==0):
                print(nums2[j-1])
                break
    elif j>=n:
        while True:
            i+=1
            count+=1
            if (count>((m+n)//2) and (m+n)%2==1) or (count>=((m+n)//2) and (m+n)%2==0):
                print(nums1[i-1]) 
                break