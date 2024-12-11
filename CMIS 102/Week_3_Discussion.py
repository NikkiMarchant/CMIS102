# Nicole Marchant CMIS 102 6980
# performs mathematical operations based on user input to check if num is even
# Used this to get random number generator https://www.geeksforgeeks.org/random-numbers-in-python/
import random


def main():
    print('Want to play a game? Try and get an even number!')
    user_operator = input("Give me one of the following operators (+,-,/,*):")
    user_operand1 = eval(input('Enter a number from -100 to 100:'))
    user_operand2 = eval(input('Enter a number from -100 to 100:'))
    user_num = 0
    random_num = random.randrange(1,101)  # used random library to get a random number between 1 and 100

    if user_operand1 < -100 or user_operand1 > 100:  # making sure user stays within range
        print("Invalid number, -100 to 100:", user_operand1)
        return
    if user_operand2 < -100 or user_operand2 > 100:  # making sure user stays within range
        print("Invalid number, -100 to 100:", user_operand2)
        return

    if user_operator == "+":
        user_num = user_operand1 + user_operand2
    elif user_operator == "-":
        user_num = user_operand1 - user_operand2
    elif user_operator == "*":
        user_num = user_operand1 * user_operand2
    elif user_operator == "/":
        if user_operand2 == 0:
            print("Don't divide by zero")  # I wanted to avoid errors that come with dividing by 0
            return
        user_num = user_operand1 / user_operand2
    else:
        print("Invalid operator")
        return
    final_num = (user_num * random_num) % 2  # Check if user_num * random_num is even
    print("Your number is:", final_num)
    if final_num == 0:
        print("Your number is even, you WIN!")
    else:
        print("You number is odd, you LOSE!")

    return


main()
