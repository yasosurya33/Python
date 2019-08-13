num=int(input())
sam=input().split()[:num]
for i in sam:
    if sam.count(i)==1:
        print(i)
