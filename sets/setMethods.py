s={1,2,3,4,5,6,6,7,8,8,9}

s.remove(2) #removes hash values
s.discard(3) #same as remove

print(s)

s.pop() #removes random

s.clear()

print(s)


a={1,2,3,4,5}
b={4,5,6,7,8}

#print(a.union(b))

#union shortcut
print(a|b)

#intersection for common part
#print(a.intersection(b))                   #------------4 and 5 is common

#intersection shortcut
print(a&b)

#difference
print(a.difference(b))
print(b.difference(a))

#difference shortcut
#print(a-b)

#symmetric difference - removes common part

#print(a.symmetric_difference(b))

#shortcut for symmetric difference
print(a^b)


#we can also use compount operations to do operations in A or B itself
b-=a
print(b)
