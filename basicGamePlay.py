__author__ = 'lschubert'
f = open("output.txt","r")

input = f.readlines()
board = [[],[],[],[],[],[],[],[]]
for i in range(0,8):
    text = input[i]
    j =0
    row  = ["","","","","","","",""]
    for k in text:

        #print k
        if k != "\n":

            row[j] = k
        j += 1
    board[i] = row

for k in board:
    i =0
    s = ""
    for i in range(0,8):
        s = s+  " "+ k[i]
        i +=1
    print s