print('Welcome to Dharavi Bank ATM')
restart=('Y')
chances = 3
balance =  100.00
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Transfer Money\n')
            print('Please Press 5 To Return Card\n')
            option = int(input('What Would you like to choose?'))

            #To check the balance
            if option == 1:
                print('Your Balance is Rs.',balance,'\n')
                restart = input('Would You you like to go back (y / yes or n/ no)? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break

            #To withdraw money     
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? '))
                if withdrawl % 10 == 0 and withdrawl <= balance:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Rs.',balance)
                    restart = input('Would You you like to go back (y / yes or n/ no)? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl %10 != 0:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))
                else:
                       print("you don't have sufficient balance") 

            #To pay in or add money to your account
            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                if Pay_in %10 ==0: 
                        balance = balance + Pay_in
                        print ('\nYour Balance is now Rs.',balance)
                else :
                        print("please pay in a valid amount")
                restart = input('Would You you like to go back (y / yes or n/ no) ? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break


            #To transfer money
            elif option == 4:
                trans =input("please enter account number(14-digits) or mobile number (10 - digits):")
                transfer = int(input("please enter the amount you wanted to transfer"))
                if transfer % 10 == 0 and transfer <= balance:
                        balance = balance - transfer
                        print("money transfered to",transfer)
                        print ('\nYour Balance is now Rs.',balance)
                        restart = input('Would You you like to go back (y / yes or n/ no)? ')
                        if restart in ('n','NO','no','N'):
                                print('Thank You')
                                break
                elif transfer %10 != 0:
                        print('Invalid Amount, Please Re-try\n')
                        restart = ('y')
                elif transfer == 1:
                        transfer= float(input('Please Enter Desired amount:'))
                else:
                        print("you don't have sufficient balance")

            #To return your card
            elif option == 5:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
