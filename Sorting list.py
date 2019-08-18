from collections import Counter


num = int(input())
sam =list(set(map(int,input().split()[:num])))
sam.sort()
for i in sam:
  print(i,end=" ")
