
# Add two numbers

num1 = 5
num2 = 10
sum  = num1 + num2

#print("sum of: ", num1, " and ", num2, " is: ", sum)


# Taking user input.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

#sum = float(n1) + float(n2)

#print("sum of: ", n1, " and ", n2, " is ", sum)

# Add two numbers using functions
def add(a, b):
    return a + b

def printNow(a, b, sum):
    print("sum of: ", a, " and ", b, " is ", sum)
    return None

#sum = add(int(n1), int(n2))
#printNow(n1, n2, sum)

# Add two numbers using add functions

#import operator
#sum = operator.add(n1, n2)
#printNow(n1, n2, sum)

# Add 2 numbers usinglambda
lambdaSum = lambda a, b : a + b
s
um = lambdaSum(n1, n2)
#printNow(n1, n2, sum)


# Add 2 numbers using recursion
def addRecursion(a, b):
    return addRecursion(a + 1, b- 1) if b != 0 else a

def addRecursion2(a, b):
    if (b == 0):
        return a
    return addRecursion(a+1, b-1)

sum = addRecursion(n1, n2)
printNow(n1, n2, sum)

