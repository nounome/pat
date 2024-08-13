
m=int(input())

id,ins,outs=[],[],[]
for i in range(m):
    info=input().split()
    id.append(info[0])
    ins.append(info[1])
    outs.append(info[2])

early=float('inf')
late=-float('inf')

for i in range(len(ins)):
    timei=list(map(int,ins[i].split(':')))

    tamp=timei[0]*3600+timei[1]*60+timei[2]

    if tamp<early:
        early=tamp
        index_early=i


for i in range(len(outs)):
    timei=list(map(int,outs[i].split(':')))

    tamp=timei[0]*3600+timei[1]*60+timei[2]

    if tamp>late:
        late=tamp
        index_late=i

print(id[index_early],id[index_late])



    