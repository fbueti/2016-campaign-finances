__author__ = 'fbueti'

white = []
black = []
for i in range(1600,2000,-128):
    val = i/10000.0
    print("\"rgba(255,255,255," + str(val) + ")\",")
for j in range(2000,7000,128):
    val = j/10000.0
    print("\"rgba(0,0,0," + str(val) + ")\",")

# .16 -> .2 -> .2 -> .7