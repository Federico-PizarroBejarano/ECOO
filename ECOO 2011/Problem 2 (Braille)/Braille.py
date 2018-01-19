bns = (0, 1, 5, 3, 11, 9, 7, 15, 13, 6, 14, 17, 21, 19, 27, 25, 23, 31, 29, 22, 30, 49, 53,\
       46, 51, 59, 57)
alph = (" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

def add(a, b, c):
    d = []
    for i in range(len(a)):
        d.append(a[i] + b[i] + c[i])
    return d
    
num = input()
lines = []
done = []

for line in range(num):
    a = list(raw_input())
    for i in range(len(a)):
        if i%2 == 0 and a[i] == "x":
            if line%3 == 0:
                a[i] = 1
            if line%3 == 1:
                a[i] = 4
            if line%3 == 2:
                a[i] = 16
        elif i%2 == 1 and a[i] == "x":
            if line%3 == 0:
                a[i] = 2
            if line%3 == 1:
                a[i] = 8
            if line%3 == 2:
                a[i] = 32
        elif a[i] == "o":
            a[i] = 0
    a = [a[i:i + 2] for i in range(0, len(a), 2)]
    for i in range(len(a)):
        a[i] = sum(a[i])
    lines.append(a)
    if len(lines) == 3:
        done.append(add(lines[0], lines[1], lines[2]))
        lines = []

for i in range(len(done)):
    for j in range(len(done[i])):
        done[i][j] = alph[bns.index(done[i][j])]
    print "".join(done[i])
