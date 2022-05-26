from fileinput import close


f = open("newfile.txt", "w")
f.write("Python is easy to lear and understand")
f = open("newfile.txt", "a")
f.write("\n create python programs")
f.write("\n by creating more python programs")
f.write("\n to be atleast intermediate level in python")
f = open("newfile.txt", "r")
close()