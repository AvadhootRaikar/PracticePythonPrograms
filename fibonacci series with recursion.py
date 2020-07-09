def fib(n):
    if n==1:      #1st term is 0
        return 0
    elif n==2:
        return 1  #2nd term is 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("enter last term required :"))
for i in range (1,n+1):     #list with value 1...to...n
    print(fib(i),end=',')
print("....")
