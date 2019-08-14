a,b=map(int,input().split())
nam=input().split()[:a]
dub=[]
for i in nam:
    dub.append(int(i))
dub.sort()
print(dub[-b])
