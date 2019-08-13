num=int(input())
dub=map(int,input().split()[:num])
dub1=[]
for i in dub:
    dub1.append(int(i))
dub1.sort()
dub1.reverse()
for i in dub1:
    print(i)
