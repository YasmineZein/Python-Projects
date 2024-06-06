#Rock-Paper-Scissors
import random
print("\n-----------------------------------------\n       Rock-Paper-Scissors Game\n\t   You vs. Computer \n\t       Good luck! \n")
#The main loop
while True:
    
    choices = ['Rock','Paper','Scissors']
    print("\nEnter your choice: ")

    #Loop to show the choices
    for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
    
    #Ask the user how many rounds they want to play
    try:
        n = int(input("How many rounds do you wish to play? "))
    except ValueError:
        print("\n ***Invalid input. Please enter a number***")
        continue
    counter = 0
    you = 0
    computer = 0
    #Loop to play the rounds
    while counter<n:
        #Loop to get the users choice
        try:
            user = int(input("\nEnter the number of your choice: "))
        except ValueError:
            print("\n ***Invalid input. Please enter a number***")
            continue

        #The game
        if 1 <= user <= len(choices):
            selected_choice = choices[user - 1]
            #Computer's choice
            random_choice = random.choice(choices)

            print(f"\nYou: {selected_choice}")
            print(f"Computer: {random_choice}")

            if (selected_choice == 'Rock' and random_choice == 'Paper') or (selected_choice == 'Paper' and random_choice == 'Scissors') or (selected_choice == 'Scissors' and random_choice == 'Rock'):
                print("\n           ***You lost!***")
                computer += 1
                print(f"Your score: {you}\nComputer score: {computer}")
            elif (selected_choice == 'Rock' and random_choice == 'Scissors') or (selected_choice == 'Paper' and random_choice == 'Rock') or (selected_choice == 'Scissors' and random_choice == 'Paper'):
                print("\n           ***You won!***")
                you += 1
                print(f"Your score: {you}\nComputer score: {computer}")
            else:
                print("\n           ***Draw!***")
                print(f"Your score: {you}\nComputer score: {computer}")
        else:
            print("\n ***Invalid input! Please enter a number between 1 and 3***")
            continue
        counter+=1
    #Check if the user won or lost
    if you > computer:
        print("\n-----------------------------------------\n          You won the match!")
    elif computer > you:
        print("\n-----------------------------------------\n          You lost the match!")
    else:
        print("\n-----------------------------------------\n          It's a draw!")

    #Loop to ask if the user wants a rematch
    while True:
        try:
            rematch = input("-----------------------------------------\n    Do you want a rematch?(Yes/No)" ).lower()
        
            if rematch == 'yes':
                break
            elif rematch == 'no':
                print(f"\n   The final score is: You: {you} Computer: {computer}")
                print("\n   Thank you for playing! See you soon!\n-----------------------------------------")
                raise SystemExit
            else:
                print("\n ***Invalid input! Enter 'Yes' or 'No'***\n")
                continue

        except ValueError:
            print("\n ***Invalid input! Please enter 'Yes' or 'No'***\n")
            continue