
game1=list(map(float,input().split()))
game2=list(map(float,input().split()))
game3=list(map(float,input().split()))


max1=max(game1)
max1_index=game1.index(max1)

max2=max(game2)
max2_index=game2.index(max2)

max3=max(game3)
max3_index=game3.index(max3)

ans= (game1[max1_index]*game2[max2_index]*game3[max3_index]*0.65-1)*2
ans=round(ans,2)

dict={0:'W',1:'T',2:'L'}

print(dict[max1_index],dict[max2_index],dict[max3_index],ans)