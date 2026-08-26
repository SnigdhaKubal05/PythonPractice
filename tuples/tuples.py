tup=(1,2,3,4)

#tup[0]=2        #immutable - cannot change value outside tuple like this
print(tup)


t=(1,2,3,4,"snigdha",True)
for i in t:
    print(i)

#unpacking
a,b,c,d=(1,2,3,4)
print(a)

#methods
x=(1,2,3,4,5,5,5)
index=x.index(5)  #will print index of 5

print(index)

#count - counting occurances

c-x.count(5)
print(c)