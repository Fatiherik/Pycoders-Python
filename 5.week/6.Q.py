def calculate():
    try:
        first_number=float(input("Enter your first number: "))
        operation = input('''Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ''')
        second_number=float(input("Enter your second number: "))

        if operation=="+":
            print("Result: "+str(first_number+second_number))
        elif operation=="-":
            print("Result: "+str(first_number-second_number))
        elif operation=="*":
            print("Result: "+str(first_number*second_number))
        elif operation=="/":
            print("Result: "+str(first_number/second_number))
        else:
            print("please run the program again and enter one of them as an operator: + - * /")

    except ZeroDivisionError:
        print("Second number can not be zero...")

    except ValueError:
        print("Please enter a number...")

    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()

