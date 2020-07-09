#Gives Factorial of a number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("enter a number"))
result=fact(n)
print(result)


