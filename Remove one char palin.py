def palin(x):
    sam1 = x
    l = int(len(sam1))
    i = 0
    lab = 0
    while i < (l // 2):
        if (sam1[i] == sam1[l - 1 - i]):
            lab = 1
            i += 1
        else:
            break
    if lab == 1:
        return 1
    else:
        return 0


nam = input()
dub = []
sam=''
for i in nam:
    dub.append(i)
dub1=dub.copy()
lab1=0
for i in range(len(dub)):
    dub[i]=""
    for i in dub:
        sam+=i
    if palin(sam)==1:
        lab1=1
    sam=""
    dub=dub1.copy()
if lab1==1:
    print("YES")
else:
    print("NO")
