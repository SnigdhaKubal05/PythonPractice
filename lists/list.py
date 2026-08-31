#lists are immutable and hetrogeneous in nature.
#can store any datatype 
a=[1,2,3,4,5,6]

print(a)
print(a[-1])

#traversing
#1st way - indexing, it prints INDEXES of lists values
for i in range(len(a)):
    print(i)
    #print values
    print(a[i])

#2nd way - directly values
for i in a:
    print(i)



l=[1,2,3,4,5]
for i in range(len(l)):
    print(i)