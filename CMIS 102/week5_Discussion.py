#  Nicole Marchant CMIS 102 6980 Week 5 Discussion
# Computes the number of hours spent gaming.

def question(day: str):
    # https://realpython.com/python-formatted-output/ used this website for .format method
    user_input = eval(input('How many hours did you spend playing video games on {0}:'.format(day)))
    return user_input


def main():
    days = 0
    total = 0
    days_dict = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    while days < 7:  # calls function 7 times and ask user how many hours they play video games a day
        days = days + 1
        answer = question(days_dict.get(days))  # got data from the dictionary
        total = total + answer  # added all the user inputs

    print('You have played {0} hours this week.'.format(total))


if __name__ == '__main__':
    main()
