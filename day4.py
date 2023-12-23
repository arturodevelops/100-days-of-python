import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options= [rock,paper,scissors]

user_choice = int(input("What do you chose? \n0.Rock \n1.Paper \n2.Scissors "))

if int(user_choice) > 2 or int(user_choice) < 0:
    print("Error: invalid choice")

computer_choice = random.randint(0,2)

if user_choice <= 2:
    print('You choose: \n' + options[user_choice])
    print('Computer choose: \n' + options[computer_choice])


if user_choice == computer_choice:
    print("It's a tie")
elif user_choice > 2:
    print("You chose an invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
    print("User won!")
elif user_choice == 1 and computer_choice == 0:
    print("User won!")
elif user_choice == 2 and computer_choice == 1:
    print("User won!")
elif computer_choice == 2 and user_choice == 1:
    print("Computer won!")
elif computer_choice == 0 and user_choice == 2:
    print("Computer won!")
elif computer_choice == 1 and user_choice == 0:
    print("Computer won!")

# #Angela's solution
# if user_choice == computer_choice:
#     print("It's a draw")
# elif user_choice > 2:
#     print('You typed an invalid number')
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice==2:
#     print("You lost")
# elif computer_choice > user_choice:
#     print("You lost")
# elif user_choice > computer_choice:
#     print("You win")    

    


