
#题意有点难懂，只要想着：尽可能平分每一段长度，且底部长度要大于等于左右两边

s=input()
n=len(s)

k=n//3 if n%3!=0 else n//3-1
left=s[:k+1]
right=s[n-(k+1):n]
mid=s[k:n-(k+1)+1]

right=right[::-1]

for i in range(len(left)-1):
    cs=' '*(len(mid)-2)
    res=left[i]+cs+right[i]
    print(res)
print(mid)
