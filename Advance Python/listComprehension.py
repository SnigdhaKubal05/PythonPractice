#list comprehension
l=[i for i in range(0,21) if i%2==0]
#do this - for this situation - in this condition

print(l)

#ternary operation

x,y=5,5

demo=x if x>y else y

print(demo)


#dictionary comprehension

d={i: i+1 for i in range(0,11) }
print(d)