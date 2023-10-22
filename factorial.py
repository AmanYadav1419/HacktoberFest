f=int(input("Enter any number"))
def fact(num):
    if num <= 0:
        return 0
    fact_=1
    for i in range(1,num+1):
        fact_*=i
    return fact_
print("The factorial of the number is",fact(f))
