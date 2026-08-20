
#traversal Loop
for i in range (1,10):
    print(i)

#filtering loop
for i in range(1,10):
    if i>2:
        print(i)

#accumulator loop
answer=2
for i in range(1,answer):
    answer+=answer
    print(answer)


#MULTIPLICATION TABLE
num=2
for i in range(1,11):
    print(2*i)


l=["Snigdha","Sanvi","Human","Robot"]
for items in l:
    print("Hello", items)


for i in range(5, 0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(4):
    for j in range(5):
        print("*",end=" ")
    print()