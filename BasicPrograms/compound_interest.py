"""
CI = (P + P * R/100)^t
or
P (1 + R/100)^t
"""

def compound_interst(p, r, t):
    return p * pow((1 + r/100), t)- p

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time in years: "))

print("Compound Interest: ", compound_interst(p, r, t))


for i in range(t):
    print(i)
# if t = 5; range will be 0  to 4.

