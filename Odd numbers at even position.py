num=int(input())
sam=input().split()[:num]
dub1=[]
for i in range(0,num):
    if i%2==0:
        if not int(sam[i])%2==0:
            dub1.append(sam[i])
    else:
        if int(sam[i])%2==0:
            dub1.append(sam[i])
for i in dub1:
    print(i,end=" ")
