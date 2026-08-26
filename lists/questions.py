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

#greatest element with its index

l=[24,29,5,78,100,65]

largest=l[0]
index=0

for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your largest element is {largest} and its index is {index}")


#largest and second largest
a=[12,16,13,19,17]

largest=a[0]
second_largest=a[0]

for i in a:
    if i>largest:
        second_largest=largest
        largest=i

    elif i>second_largest:
        second_largest=i

print(second_largest,largest)
"""

#check if list is sorted or not

b=[4,5,6,7,8]

for i in range(len(b)-1): #because if iteration goes till last value of index i.e 8 in the above list then it will give error of Out of range list
    if b[i]<b[i+1]:
        continue
    else:
        print("list aint sorted")
        break
else:
    print("list is sorted")