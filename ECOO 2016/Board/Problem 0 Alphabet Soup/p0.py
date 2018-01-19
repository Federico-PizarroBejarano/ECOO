f = open("DATA01.txt", "r")

nList = []
soupList = []
for i in range(5):
  nList.append(int(f.readline().strip()))
  soupList.append([i for i in f.readline().strip()])

sortedLists = [sorted(i) for i in soupList]

for i in range(5):
  if soupList[i] != sortedLists[i]:
    print (nList[i]), "NOT IN ORDER"
  else:
    print (nList[i]), "IN ORDER"

f.close()
