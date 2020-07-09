number=int(input("Enter a number :"))
number2=str(number)
reversenumber=number2[::-1]

if reversenumber==number2:
    print("It is a palindrome number")
else:
    print("It is  not a palindrome number")
    
