import os

def errorless_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Hoes and problems ain't nothin' but numbers. Literally. Enter a damn number.")


def calculator():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Life ain't nothin' but hoes and problems.")
    num1 = errorless_float("How many hoes?")
    num2 = errorless_float("How many problems?")
    print("Please enter the operation you would like to perform:")
    print("1. Hoes plus problems?")
    print("2. Hoes minus problems?")
    print("3. Total problems if each hoe has that many problems?")
    print("4. Hoes per problem?")
    operation = int(input())
    if operation == 1:
        print("You've got", num1 + num2 , "hoes and problems.")
    elif operation == 2:
        if num1 >= num2:
            print("If problems delete hoes, you've got", num1 - num2 , "hoes left.")
        else:
            print("If hoes delete problems, you've got", num2 - num1 , "problems left.")
    elif operation == 3:
        print("You've got", num1 * num2 , "problems.")
    elif operation == 4:
        print("For each problem, there are", num1 / num2, "hoes.")
    else:
        print("Bitches must be trippin' you up.")
    print("I sleep.")

calculator()

