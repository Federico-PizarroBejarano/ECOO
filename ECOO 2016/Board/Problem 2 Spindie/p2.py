f = open("DATA21.txt.", "r")

for i in xrange(10):
  n = int(f.readline().strip())
  numbers = map(int, f.readline().strip().split())
  possible = map(int, f.readline().strip().split())
  multiples = set()
  add = set()
  total = set()
  ans = ""

  for number1 in numbers:
    for number2 in numbers:
      total.add(number1*number2)
      total.add(number1+number2)
  
  for thing in possible:
    check = 0
    for number in numbers:
      check1 = thing*1.0/number
      check2 = thing-number
      if check1 == int(check1):
        if int(check1) in total:
          ans += "T"
          check = 1
          break
      if check2 in total:
        ans += "T"
        check = 1
        break


    if check == 0: ans += "F"

  print ans

f.close()
