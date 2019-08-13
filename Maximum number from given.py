nam=int(input())
sam=input().split()[:nam]
sam.sort()
sam.reverse()
for i in sam:
    print(i,end="")
