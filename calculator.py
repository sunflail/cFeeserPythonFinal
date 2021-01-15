#!/usr/bin/env python3
'''
This is a calculator. It can only do what a calulator can do.
'''


#add function
def add(NUM1,NUM2):
    return NUM1+NUM2

#subtract function
def subtract(NUM1,NUM2):
    return NUM1-NUM2

#multiply function
def multiply(NUM1,NUM2):
    return NUM1*NUM2

#divide function
def divide(NUM1,NUM2):
    try:
        # result = mustBeNumber(str(NUM1/NUM2))
        result = NUM1/NUM2
        return result
    except (ZeroDivisionError):
        print("Cannot divide by zero, please try again.")
        exit(0)

#int or float function
def mustBeNumber(numToCheck):
    if "." in numToCheck:
        return float(numToCheck)
    else:
        return int(numToCheck)


def user_input():
    while True:
        try:
            NUM1 = input("Please enter the first number: ")
            NUM1 = mustBeNumber(NUM1)
            if type(NUM1) == int or float:
                break
        except:
            print("Please enter an int or a float only.")
    while True:
        try:
            NUM2 = input("Please enter the second number: ")
            NUM2 = mustBeNumber(NUM2)
            if type(NUM2) == int or float:
                break
        except:
            print("Please enter an int or a float only.")
    return NUM1, NUM2

def main():
    # must accept floats/integers as user input
    NUM1, NUM2 = user_input()
    while True:
        OPERATOR = input("Please enter +, -, /, *, or q to quit: ")
        if OPERATOR.strip() == "+":
            result = add(NUM1, NUM2)
            break
        elif OPERATOR.strip() == "-":
            result = subtract(NUM1, NUM2)
            break
        elif OPERATOR.strip() == "/":
            result = divide(NUM1, NUM2)
            break
        elif OPERATOR.strip() == "*":
            result = multiply(NUM1, NUM2)
            break
        elif OPERATOR.strip().lower() == "q":
            print("Thank you, have a nice day.")
            exit(0)
        else:
            print("Invalid. Try again.")
    return f'{NUM1} {OPERATOR} {NUM2} = {result}'
    # print(result)
    # return result

if __name__ == '__main__':
    main()
