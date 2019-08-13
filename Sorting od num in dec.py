num=int(input())
dub=input().split()[:num]
dub.sort()
dub.reverse()
for i in dub:
    print(i)
