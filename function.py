#Functions

#Simple
def function():
    print("This is our first function")
function()

#Returning
def returning():
    return "This is a result!"
result = returning()
print(result)

#Returning multiple values
def multival():
    return "this is a rresult,",2
print(multival())

#Parameters
def parameters(a):
    print(a)
parameters("This is a parameter")

#Default parameters
def default_param(a, b = 4, c = 5):
    return a + b + c
result = default_param(3)
print(result)

#Doble parameters WATEFAC
def f(a):
    def g(b):
        return a * b
    return g
print(f(5)(2))

#Recursive
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#Lambda
f = lambda x, y: x + y
print(f(2,3))