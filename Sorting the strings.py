a=int(input())
num=input().split()[:a]
dub=[]
for i in num:
    dub.append(i.lower())
dub.sort()
print("\n".join(dub))
