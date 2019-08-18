num = int(input())
sam = input().split()[:num]
dub=[]
for i in sam:
  if not i in dub:
    dub.append(i)
print(" ".join(dub))
