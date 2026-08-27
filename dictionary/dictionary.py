#also called as Hashmap in other languages

#dictionary has key columns

d={}
print(type(d))

dict={10:100,20:200,30:300,40:400}
print(dict)

#updating
dict[10]=1000
print(dict)

#Creating key-value
dict.update({50:500})
dict[60]=600

print(dict)

del dict[10]
print(dict)


#Traversing
a={1:10,2:20,3:30,4:40}
for i in a.values():              #values method helps to retrieve values directly not keys
    print(i)        #keys 
    #print(a[i])     #values


help(dict)
