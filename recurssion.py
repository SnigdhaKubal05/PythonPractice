def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

#n=int(input("Enter a number to find factorial: "))
n=4

print(f"Factorial is {factorial(n)}")