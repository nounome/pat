
nums=int(input())
postorder=list(map(int,input().split()))
inorder=list(map(int,input().split()))

childs=[[] for i in range(3000+1)]   # 阶段一：未说编号为1-nums，所以取最大节点数30，两测试点未通过   阶段二：最大节点数并不意味着是最大编号数，取3000

def buildTree(postord,inord):
    if len(postord)==1:
        return postord[0]
    if len(postord)<=0:
        return 

    root=postord[-1]

    index=inord.index(root)

    leftchild_inord,rightchild_inord=inord[:index],inord[index+1:]
    leftchild_postord,rightchild_postord=postord[:len(leftchild_inord)],postord[len(leftchild_inord):len(leftchild_inord)+len(rightchild_inord)]

    childs[root].append(buildTree(leftchild_postord,leftchild_inord))
    childs[root].append(buildTree(rightchild_postord,rightchild_inord))

    return root

root=buildTree(postorder,inorder)


nodes=[root]
res=[]
while True:
    nodescopy=[]
    if nodes:
        res+=[x for x in nodes]

    nodescopy+=[x for node in nodes for x in childs[node] if x is not None]
    nodes=nodescopy

    if not nodes: break

res=[str(x) for x in res]
print((' ').join(res))
