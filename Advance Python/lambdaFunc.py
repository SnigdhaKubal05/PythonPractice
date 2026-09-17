""""
lambda is a keyword in Python that is used to create small anonymous functions.
It can take any number of arguments,
but can only have one expression.

The expression is evaluated and returned.
Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
"""

add = lambda a,b:a+b

print(add(5,5))

#LAMBDA IN TERNARY OPERATOR

statement=lambda a : "even" if a%2==0 else "odd"

print(statement(5))