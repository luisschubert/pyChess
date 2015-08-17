__author__ = 'lschubert'
# R N B Q K B N R
whiteBack = ["B","9","A","8","7","A","9","B"]
whitePawn = ["C","C","C","C","C","C","C","C"]
# R N B K Q B N R
blackBack = ["5","3","4","1","2","4","3","5"]
blackPawn = ["6","6","6","6","6","6","6","6"]

empty = ["E","E","E","E","E","E","E","E"]


f = open("output.txt", "w")


#white back
for i in whiteBack:
    f.write(i)


f.write("\n")
#white pawns
for i in whitePawn:
    f.write(i)
f.write("\n")
#empty cells
for i in range(0,4):
    for k in empty:
        f.write(k)
    f.write("\n")

#black pawns
for i in blackPawn:
    f.write(i)
f.write("\n")
#black back
for i in blackBack:
    f.write(i)
f.write("\n")



f.close()