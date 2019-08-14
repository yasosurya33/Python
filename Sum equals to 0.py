num=int(input())
sam=input().split()[:num]
dub1=[]
for i in sam:
    for j in range(num):
        if not sam.index(i)==j:
            if int(i)+int(sam[j])==0:
                dub1.append((i,sam[j]))
for i in range(1):
    for j in range(2):
        print(dub1[i][j],end=" ")
