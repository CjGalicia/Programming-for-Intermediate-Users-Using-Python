f = open("newfile.txt", "r")
print(f.read())

g = open("newfile1.txt", "r")
print(g.readline())

h = open("newfile2.txt", "r")
for x in h:
    print(x)