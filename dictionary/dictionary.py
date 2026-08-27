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