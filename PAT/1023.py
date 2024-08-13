
num=input()
sorted_num=sorted([x for x in num])

doublenum=int(num)*2

sorted_doublenum=sorted([x for x in str(doublenum)])

if sorted_num==sorted_doublenum:
    print('Yes')
else:
    print('No')
print(doublenum)

