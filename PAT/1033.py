#有一个测试点超时，未AC

cap,dist,avg,n=map(int,input().split())

infos=[]
for i in range(n):
    info=list(map(float,input().split()))
    infos.append(info)

#单价、距离
infos.sort(key=lambda x:x[1])


def dfs(lucheng,you,sumcost,cur_price):   #走的距离、剩余油量、总花费、该站点油价
    global maxdist
    if lucheng==infos[-1][1]:  #最后一个加油站  整数==浮点数？
        maxdist=max(maxdist,lucheng+cap*avg)
        if lucheng+you*avg>=dist:
            res.append(round(sumcost,2))
        elif lucheng+cap*avg<dist:    #到达不了终点  测试点1
            pass
        else:
            addcost=(dist-(lucheng+you*avg))/avg*cur_price
            res.append(round(sumcost+addcost,2))
 
        return


    max_lu=lucheng+cap*avg

    zhandian=[]
    for info in infos:
        if lucheng<info[1]<=max_lu:
            zhandian.append(info)    
        elif info[1]>max_lu:
            break
    
    if not zhandian:return   ##存疑

    for p,juli in zhandian:
        if juli==dist:     #下一个加油站就是目的地了，无论如何只需加到刚好能到的油量    测试点4！！！！很难想
            if you*avg+lucheng<juli:    #当前油量还不够到目的地
                next_lu=juli-lucheng
                addcost=(next_lu-you*avg)/avg*cur_price
                dfs(juli,0,sumcost+addcost,p)
            else:         #此情况测试样例中应该不存在，因此直接pass
                pass

        elif p>cur_price:      #当前油价小于下一站，当前站点加满
            next_lu=juli-lucheng
            addcost=(cap-you)*cur_price  #加油费
            next_you=cap-(next_lu/avg)

            dfs(juli,next_you,sumcost+addcost,p)
        else:
            if you*avg+lucheng>=juli:   #当前油量能够到达下一个站点
                next_you=you-(juli-lucheng)/avg
                dfs(juli,next_you,sumcost,p)
            else:     
                next_lu=juli-lucheng
                addcost=(next_lu-you*avg)/avg*cur_price  #加油费
                dfs(juli,0,sumcost+addcost,p)

if infos[0][1]!=0:
    print('The maximum travel distance = 0.00')  #测试点2
else:

    res=[]
    maxdist=-1
    dfs(0,0,0,infos[0][0])

    if res:
        print('{:.2f}'.format(min(res)))    #注意min(res)可能只有一位小数  测试点3、4、6
    else:
        print(('The maximum travel distance = {:.2f}').format(maxdist))