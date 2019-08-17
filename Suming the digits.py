sam=input()
l=len(sam)
dub=[]
sum=0
for i in range(l+1):
    for i in range(i):
        sum+=int(sam[i])
print(sum)
