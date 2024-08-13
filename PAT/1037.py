
nc=int(input())

coupon=list(map(int,input().split()))

np=int(input())
product=list(map(int,input().split()))

coupon.sort(reverse=True)
product.sort(reverse=True)

coupon_positive=[x for x in coupon if x>0]
coupon_nagetive=[x for x in coupon[::-1] if x<=0]   #负数从小到大

product_p=[x for x in product if x>0]
product_n=[x for x in product[::-1] if x<=0]

value=0
for i in range(min(len(coupon_positive),len(product_p))):
    value+=coupon_positive[i]*product_p[i]

for i in range(min(len(coupon_nagetive),len(product_n))):
    value+=coupon_nagetive[i]*product_n[i]

print(value)




# cur=0
# n=len(product)
# value=0
# for youhui in coupon:
#     if youhui>0:
#         if product[cur]>0 and 0<=cur<n:
#             value+=youhui*product[cur]
#             cur+=1
#         else:



