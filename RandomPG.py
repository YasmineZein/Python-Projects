import random
import string

print("\n------------------------------\nWelcome to Yasmine's Random Password Generator!\n")
#Password difficulty
def Difficulty ():
    difficulty = input("How difficult do you want your password?\n1.Weak(4-6)\n2.Good(6-8)\n3.Strong(8-10)\n4.Very Strong(more than 10)\nSelect(1/2/3/4): ")
    if difficulty == "1":
        return "easy"
    elif difficulty== "2":
        return "Good"
    elif difficulty == "3":
        return "Strong"
    elif difficulty == "4":
        return "Very Strong"
    else:
        print("\nInvalid input. Please enter a number between 1 and 4\n----------------------------------\n")
        return Difficulty()

#User input
difficulty = Difficulty()
def user_in ():
    
    if difficulty == "easy":
        try:
            length = int(input("Enter the length of the password(4-6): "))
            if length < 4 or length > 6:
                print("\nPassword must be 4 to 6 characters long\n----------------------------------\n")
                return user_in()
            else:
                return length
                
        except ValueError:
            print("\nInvalid input. Please enter a number\n----------------------------------\n")
            return user_in()
    elif difficulty == "Good":
        try:
            length = int(input("Enter the length of the password(6-8): "))
            if length < 6 or length > 8:
                print("\nPassword must be 6 to 8 characters long\n----------------------------------\n")
                return user_in()
            else:
                return length
                
        except ValueError:
            print("\nInvalid input. Please enter a number\n----------------------------------\n")
            return user_in()
    elif difficulty == "Strong":
        try:
            length = int(input("Enter the length of the password(8-10): "))
            if length < 8 or length > 10:
                print("\nPassword must be 8 to 10 characters long\n----------------------------------\n")
                return user_in()
            else:
                return length

        except ValueError:
            print("\nInvalid input. Please enter a number\n----------------------------------\n")
            return user_in()
    elif difficulty == "Very Strong":
        try:
            length = int(input("Enter the length of the password(more than 10): "))
            if length < 10:
                print("\nPassword must be more than 10 characters long\n----------------------------------\n")
                return user_in()
            else:
                return length
        except ValueError:
            print("\nInvalid input. Please enter a number\n----------------------------------\n")
            return user_in()
    else:
        return user_in()


#Generate Password

length1 = user_in()

def password():
    charachters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    random_password = ''.join(random.choice(charachters) for _ in range(length1))
    return random_password

#Display Password
print("Your Password is: " + password() + "\nThank you for using Yasmine's Random Password Generator!\n----------------------------------\n" )
