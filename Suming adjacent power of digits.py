sam=input()
l=len(sam)
dub=[]
sum=0
if l==1:
    sum+=int(sam[0])**2
else:
    for i in range(l-1):
        sum+=int(sam[i])**int(sam[i+1])
    else:
        sum+=int(sam[-1])**int(sam[0])
print(sum)
