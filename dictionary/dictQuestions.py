#1. merging two dictionaries
a={10:100,20:200,30:300,40:500}
b={40:400,60:600}

for i in b:
    a[i]=b[i]
print(a)

#2. sum of all values
c={1:10,2:20,3:30}
sum=0

for i in c:
    sum+=c[i]
print(sum)

#3. count frequency of a vlaues in a list using dictionary

l=[1,1,1,2,2,2,3,3,4,5]
d1={}

for i in l:
    if i in d1.keys():      #if i jaisi chiz d1.keys mein exist karti hai then,
        d1[i]+=1            #add 1 in that
    else:
        d1[i]=1

print(d1)


#4. combining 2 dictionaries by ADDING VALUES of common keys
d2={1:2,3:4,5:6}
d3={5:6,7:8}

for i in d3:
    if i in d2.keys():
        d2[i]+=d3[i]
    else:
        d2[i]=d3[i]

print(d2)
