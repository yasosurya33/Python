def res(x,y):
    while x>=0 and y>=0 and x<=a-1 and y<=a-1:
        b=sam[x][y]
        return b


a=int(input())
sam=[]
for i in range(a):
    for j in range(1):
        sam.append(input().split()[:a])
s=0
for i in range(a):
    for j in range(a):
        if sam[i][j]=="1":
            dup=[res(i+1,j),res(i,j-1),res(i-1,j),res(i,j+1),res(i+1,j+1),res(i+1,j-1),res(i-1,j+1),res(i-1,j-1)]
            if dup.count("1")==0:
                s+=1
print(s)
