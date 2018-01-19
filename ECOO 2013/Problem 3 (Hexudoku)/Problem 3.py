def checkLetter(num, numscon):
    if num.upper() == "A":
        result = 10
        numscon.append(result)
    elif num.upper() == "B":
        result = 11
        numscon.append(result)
    elif num.upper() == "C":
        result = 12
        numscon.append(result)
    elif num.upper() == "D":
        result = 13
        numscon.append(result)
    elif num.upper() == "E":
        result = 14
        numscon.append(result)
    elif num.upper() == "F":
        result = 15
        numscon.append(result)
    else:
        numscon.append(int(num))

def quad(grid, i, row):
    i = i + 1
    row = row + 1

    roz = 0
    col = 0

    if 0 < i < 5:
        col = 1
    elif 4 < i < 9:
        col = 2
    elif 8 < i < 13:
        col = 3
    elif 12 < i < 17:
        col = 4

    if 0 < row < 5:
        roz = 1
    elif 4 < row < 9:
        roz = 2
    elif 8 < row < 13:
        roz = 3
    elif 12 < row < 17:
        roz = 4    

    for k in range((roz*4-4),(roz*4)):
        for i in range((col*4-4),(col*4)):
            if number[grid][k][i] != "-" and nums.count(number[grid][k][i]) < 1:
                nums.append(number[grid][k][i])
                
closefile = open("DATA30.txt")
number = closefile.read().splitlines()
number = [number[i:i+16] for i in range(0, len(number), 16)]
filled = 0

for grid in number:
    for row in grid:
        letters = []
        for letter in row:
            letters.append(letter)
        number[number.index(grid)][grid.index(row)] = letters

for grid in range(len(number)):
    for row in range(16):
        for letter in range(16):
            if number[grid][row][letter] != "-":
                continue
            else:
                nums = []
                for i in range(16):
                    quad(grid, letter, row)
                for i in range(16):
                    if number[grid][row][i] != "-" and nums.count(number[grid][row][i]) < 1:
                        nums.append(number[grid][row][i])
                for i in range(16):
                    if number[grid][i][letter] != "-" and nums.count(number[grid][i][letter]) < 1:
                        nums.append(number[grid][i][letter])
                numscon = []
                for i in nums:
                    checkLetter(i, numscon)
                numscon = sorted(numscon, key=int)
                if len(numscon) == 16:
                    nums = []
                    numscon = []
                    continue                    
                else:
                    for i in range(16):
                        if numscon.count(i) > 0:
                            continue
                        else:
                            add = ""
                            if i == 10:
                                add = "A"
                            elif i == 11:
                                add = "B"
                            elif i == 12:
                                add = "C"
                            elif i == 13:
                                add = "D"
                            elif i == 14:
                                add = "E"
                            elif i == 15:
                                add = "F"
                            else:
                                add = str(i)
                            number[grid][row][letter] = add
                            add = ""
                            filled += 1
                            nums = []
                            numscon = []
                            break

    print filled
    filled = 0

closefile.close()
