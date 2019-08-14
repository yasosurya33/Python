def res(x,y):
    while x>=0 and y>=0 and x<=a-1 and y<=a-1:
        b=sam[x][y]
        return b


a,b=map(int,input().split())
sam=[]
for i in range(a):
    for j in range(1):
        sam.append(input().split()[:b])
samp=sam.copy()
for i in range(a):
    for j in range(b):
            dup=[res(i+1,j),res(i,j-1),res(i-1,j),res(i,j+1),]
            if "0" in dup:
                samp[i][j]=int(0)
            else:
                samp[i][j]=sam[i][j]
for i in samp:
    for j in i:
        print(j,end=" ")
    print(" ")
