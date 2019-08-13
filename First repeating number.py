num=int(input())
sam=input().split()[:num]
sum=0
for i in sam:
    if sam.count(i)>1:
        print(i)
        break
    else:
        sum+=1
if sum==num:
    print("unique")
