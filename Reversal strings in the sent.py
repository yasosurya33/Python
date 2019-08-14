nam=input().split()
for i in nam:
    nam1 = []
    for j in i[::-1]:
        nam1.append(j)
    for i in nam1:
        print(i, end="")
    print(" ",end="")
