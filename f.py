#w create & overwrite, a create & append end of the line, x create & error message if the file exist
# f=open("demo.txt", "a")
# f.write(" new line has been added")
# f.close()
# f=open("demo.txt","r")
# print(f.read())

f = open("demo1.txt", "a")
f.write("this is a new file")
f.close
f = open("demo1.txt","r")
print(f.read())