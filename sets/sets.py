a={1,2,3,4}
print(a)

print(type(a))

b={}        #empty set is dictionary
print(type(b))


c={1,3,2,4,5,6,5,5,"hello",9,"snigdha",7}       #hash value will get them in ordered because integeres has as it is hash values
print(c)

#traversing - no direct looping it will give random values depends on hash values stored by system
d={1,2,3,4,5,6,7,8}
for i in d:
    print(i)