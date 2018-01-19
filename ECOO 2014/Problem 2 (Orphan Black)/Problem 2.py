import sys

closefile = open("DATA21.txt")
def everything(closefile):
    infile = closefile.read().splitlines()  

    dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                  "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    binaryDiction = ["01000001", "01000010", "01000011", "01000100",
                     "01000101", "01000110", "01000111", "01001000",
                     "01001001", "01001010", "01001011", "01001100",
                     "01001101", "01001110", "01001111", "01010000",
                     "01010001", "01010010", "01010011", "01010100",
                     "01010101", "01010110", "01010111", "01011000",
                     "01011001", "01011010", "00100000"]
    dnalist = []
    for i in range(len(infile)):
        if i % 2 == 0:
            dnalist.append(infile[i])
    for dna in dnalist:
        dna = dna.lower()
        binaryAT = ""
        binaryCG = ""
        messageAT = []
        messageCG = []
        answer = ""
        bigger = []

        for i in dna:
            if i == "a" or i == "t":
                binaryAT += "0"
            elif i == "c" or i == "g":
                binaryAT += "1"
        for i in dna:
            if i == "c" or i == "g":
                binaryCG += "0"
            elif i == "a" or i == "t":
                binaryCG += "1"

        while len(binaryAT) > 0:
            messageAT = [binaryAT[i:i + 8] for i in range(0, len(binaryAT), 8)]
            messageCG = [binaryCG[i:i + 8] for i in range(0, len(binaryCG), 8)]
            for i in binaryDiction:
                if messageAT[0] == i:
                    making(messageAT, dictionary, binaryDiction, answer, binaryAT, bigger)
                elif messageCG[0] == i:
                    making(messageCG, dictionary, binaryDiction, answer, binaryCG, bigger)
                else:
                    continue
            binaryAT = binaryAT[1::]
            binaryCG = binaryCG[1::]
        print( max(bigger, key=len))

def making(message, dictionary, binaryDiction, answer, binary, bigger):
    for i in message:
        for j in binaryDiction:
            if i == j:
                answer += (dictionary[binaryDiction.index(i)])
    bigger.append(answer)

everything(closefile)
closefile.close()

