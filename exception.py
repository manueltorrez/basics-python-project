try:
    a = 5/0
except Exception as e:
    print(e)

#Specific
try:
    n = int(input("Enter an Integer: "))
except ValueError:
    print("That is not an integer")

#Throwing exceptions
def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not string")
a=1
try:
    RaiseException(a)
except ValueError as e:
    print(e)