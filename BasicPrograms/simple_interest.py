# si = p * r * t / 100

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print("Simple Interest: ", simple_interest(principal, rate, time))