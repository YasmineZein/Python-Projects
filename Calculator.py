
print("Yasmine's Calculator")

# A function to show the operations available
def get_ope():
    ope = input(f"----------------\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Modulus \nSelect(1/2/3/4/5): ")
    return ope

#A function for addition
def addition():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f'{a} + {b} = {a+b}')
    except ValueError: 
        print("invalid input")
        addition()
    
#A function for subtraction
def subtraction():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f'{a} - {b} = {a-b}')
        print(f'{b} - {a} = {b-a}')
    except ValueError: 
        print("invalid input")
        subtraction()

#A function for multiplication
def multiplication():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f'{a} * {b} = {a*b}')
    except ValueError: 
        print("invalid input")
        multiplication()

#A function for division
def division():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f'{a} / {b} = {a/b}')
        print(f'{b} / {a} = {b/a}')
    except ValueError: 
        print("invalid input")
        division()
    except ZeroDivisionError:
        print("Can't divide by 0")
        division()

#A function for modulus
def modulus():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f'{a} % {b} = {a%b}')
    except ValueError: 
        print("invalid input")
        modulus()

#A function to get the users wanted operation
def get_nums():
    
    userinput = get_ope()
    if userinput == "1":
        return addition()
    elif userinput == "2":
        return subtraction()
    elif userinput == "3":
        return multiplication()
    elif userinput == "4":
        return division()
    elif userinput == "5":
        return modulus()
    else:
        print("Invalid! please choose between 1-5")
        get_nums()

#The main loop
while True:
    #Loop to get the users wanted number of operations
    try:
        n = int(input("Enter number of operations needed: "))
    except ValueError:
        print("Invalid! Enter a number only")
        continue
    counter = 0
    #Loop to get the users wanted operations
    while counter < n :
        get_nums()
        counter+=1

    #Loop to ask if the user wants more operations
    repeat = input("Do you want to more operations?(Yes/No) ").lower()
    if repeat == 'yes':
        continue
    elif repeat == 'no':
        print("Thanks for using Yasmine's Calculator")
        raise SystemExit
    else:
        print("Invalid! Enter 'Yes' or 'No'")
        raise SystemExit