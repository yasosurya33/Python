num=int(input())
sam=input().split()[:num]
dub=[]
for i in range(num):
    dub.append((sam[i],i))
dub1=[]
for i in range(num):
    for j in range(1):
        if int(dub[i][0])==dub[i][1]:
            dub1.append(dub[i][0])
dub1.sort()
for i in dub1:
    print(i,end=" ")
if dub1 ==[]:
    print("-1")
