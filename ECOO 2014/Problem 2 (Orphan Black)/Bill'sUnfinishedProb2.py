inFile = open("DATA21.txt")
laRum = []
dicktionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
binaryDicktion = ["01000001", "01000010", "01000011" , "01000100", "01000101", "01000110", "01000111", "01001000", "01001001", "01001010", "01001011", "01001100", "01001101",
                  "01001110", "01001111", "01010000", "01010001", "01010010", "01010011", "01010100", "01010101", "01010110", "01010111", "01011000", "01011001", "01011010", "00100000"]

stringOne = inFile.readline().strip("\n")
stringTwo = inFile.readline().strip("\n")

for i in range(len(stringOne)):
    laRum.append(stringOne[i] + stringTwo[i])

for i in range(len(laRum)):
    if laRum[i] == "AT" or laRum[i] == "TA":
        laRum[i] = "0"
    elif laRum[i] == "GC" or laRum[i] == "CG":
        laRum[i] = "1"

start = 0
end = 7

bitString = ""
letter = ""
foundv1 = False

print len(stringOne)

for i in range(7):
    bitString = ""
    for j in range(start, end+1, 1):
        bitString = bitString + laRum[j]
    print bitString

    for k in range(len(binaryDicktion)):
        if binaryDicktion[k] == bitString:
            start = i
            end = i + 7
            letter = dicktionary[k]
        foundv1 = True
            
    print letter
    start = start + 7
    end = end + 7

#if foundv1 == True:
 #   while end < len(stringOne):
  #      for i in range(start, end, 1):
   #         bitString = bitString + laRum[i]
        
            
                

    
    
        
