f = open("DATA32.txt.", "r")

for i in xrange(10):
  n = int(f.readline().strip())
  numbers = map(int, f.readline().strip().split())
  dict1 = {}
  thing = 0
  ans = 0

  for i in xrange(n):
    num = numbers[i]
    dict1[num] = i

  for i in xrange(n-1, 0, -1):
    larger = dict1[i+1]
    smaller = dict1[i]
    
    if larger < smaller:
      thing = i
      break
  
  if thing == 0:
    print 0
  else:
    for j in xrange(thing, 0, -1):
      num = dict1[j]
      ans += num
      
      dict1[j] = 0
      for point in dict1:
        if dict1[point] < num:
          dict1[point] += 1

    print ans

f.close()
