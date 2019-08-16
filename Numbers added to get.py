a,b=map(int,input().split())
nam=input().split()[:a]
dub=nam.copy()
lab=0
for i in nam:
    dub.remove(i)
    for j in dub:
        if  int(i)+int(j) == b:
            lab=1
    dub = nam.copy()
if lab==1:
    print("YES")
else:
    print("NO")
