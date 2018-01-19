from math import floor

f = open("DATA11.txt.", "r")

for i in xrange(10):
  t, a, p, q = map(float, f.readline().split())
  n = int(f.readline())
  count = 0
  for i in range(n):
    t1, a1, p1, q1 = map(float, f.readline().split())
    if floor((t*t1 + a*a1+ p*p1 + q*q1)/100)>=50:
      count += 1
  print count
    
    
f.close()
