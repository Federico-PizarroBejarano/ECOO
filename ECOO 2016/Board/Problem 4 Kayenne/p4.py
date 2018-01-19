
f = open("DATA41.txt.", "r")

neigh = []

def dist(x, y, neigh):
  return ((x - neigh[0]) ** 2) + ((y - neigh[1]) ** 2)
  

TESTCASES = 10
for i in xrange(TESTCASES):
  dCount = 0
  rCount = 0
  Cx, Cy = map(int, f.readline().strip().split())
  for j in xrange(100): #100 neighbours
    n = f.readline().strip().split()
    n[0] = int(n[0])
    n[1] = int(n[1])
    neigh.append(n)
 
  for x in range(Cx - 50, Cx + 51):
    for y in range(Cy - 50, Cy + 51):
      if ((x - Cx) ** 2) + ((y - Cy) ** 2) <= 2500:
        distances = [[dist(x, y, neighbour), neighbour[2]] for neighbour in neigh]
        distances = sorted(distances, key=lambda x: x[0])
        r, d = 0, 0
        last = 3
        done = False
        
        while not done:
          if distances[2] == distances[last]:
            if distances[last][1] == "D":
              d += 1
            else:
              r += 1
            last += 1
          else:
            done = True
        
        if distances[0][1] == "D":
          d += 1
        else:
          r += 1
        if distances[1][1] == "D":
          d += 1
        else:
          r += 1
        if distances[2][1] == "D":
          d += 1
        else:
          r += 1
        
        if r > d:
          rCount += 1
        else:
          dCount += 1

  print round((dCount * 1.0 /(dCount + rCount)) * 1000) / 10
          
          
        

            
            
f.close()


