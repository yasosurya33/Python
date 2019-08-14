a,b=map(int,input().split())
sam=input().split()[:a]
sam1=input().split()[:b]
alb=0
for i in sam1:
    if not i in sam:
        alb=1
if alb==0:
    print("YES")
else:
    print("NO")
