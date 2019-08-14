a = int(input())
nam = map(int,input().split()[:a])
dub=[]
for i in nam:
    dub.append(int(i))
dub.sort()
dub.reverse()
sam=[]
l=len(dub)
s=1
for i in dub:
    sam.append(i)
    if s<l:
        s+=1
        sam.append("->")
for i in sam:
    print(i,end="")
