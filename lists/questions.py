"""#1. print all positive and negative numbers from the list

l=[-2,2,-5,-7,9,-46,67]

print("All positive numbers")
for i in l:
    if i>=0:
        print(i)

print("All negative numbers")

for i in l:
    if i<0:
        print(i)

#mean of all numbers - sum of all and divide with total number of values
a=[1,2,3,4]

sum=0
for i in a:
    sum=sum+i

print(sum/len(a))
"""
#greatest element with its index

l=[24,29,5,78,100,65]

largest=l[0]
index=0

for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your largest element is {largest} and its index is {index}")
