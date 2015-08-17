__author__ = 'lschubert'

'''
read line by line the input from the text file and interpret it as a matrix
'''

f = open("output.txt","r")

board = f.readlines()
colBoard = [[],[],[],[],[],[],[],[]]
for i in range(0,8):
    text = board[i]
    j =0
    row  = ["","","","","","","",""]
    for k in text:

        #print k
        if k != "\n":

            row[j] = k
        j += 1
    colBoard[i] = row
print colBoard