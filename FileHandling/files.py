p=open('string.py')

print(p.read())

r=open("snigdha.txt",'w')       #'w' overwrites
r1=open('snigdha2.txt','a')     #'a' appends to file, adds to the end of the file

r.write("Writing inside this file")
r1.write("new file with append function")

r2=open('snigdha3.txt','x')

r2.write("using x created file")
r.close()