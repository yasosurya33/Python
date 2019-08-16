a=int(input())
nam = input().split()[:a]
dub=nam.copy()
sam=[]
product=1
for i in nam:
    product=product*int(i)
for i in nam:
    sam.append(product//int(i))
for i in sam:
    print(i,end=" ")
