
n=input()

sumn=sum([int(x) for x in n])

dict={'0':'zero','1':'one','2':'two','3':'three','4':'four',
      '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}


for i in str(sumn)[:-1]:
    print(dict[i],end=' ')

print(dict[str(sumn)[-1]])