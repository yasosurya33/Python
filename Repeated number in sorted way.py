nam=int(input())
sam=input().split()[:nam]
sam.sort()
dub=[]
for i in sam:
    if sam.count(i)>1:
        dub.append(i)
dub1=[]
for i in dub:
    if i not in dub1:
        dub1.append(i)
for i in dub1:
    print(i,end=" ")
