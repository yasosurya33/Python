a,b=map(int,input().split())
sam=[]
for i in range(a):
    sam.append(input().split())
dub=sam[0]
for i in range(a-1):
    for j in range(b):
        if sam[i+1][j] in dub:
            dub.append(sam[i+1][j])
nam=[]
for i in dub:
    if dub.count(i)>=a:
        if i not in nam:
            nam.append(i)
            print(i,end=" ")
