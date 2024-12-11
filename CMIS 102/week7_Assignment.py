# Nicole Marchant CMIS 102 6980 August 1, 2023,
# This program calculates a persons shared cost of a road trip
# all currency is in USD


def main():
    food = []
    gas = []
    people = eval(input('Number of people on the trip: '))  # get user input for people and days
    days = eval(input('NUmber of days of the trip: '))
    for value in range(days):  # loop for number of days entered and get costs
        food.append(eval(input(f'Enter the total cost of food for day {value + 1}: ')))
        gas.append(eval(input(f'Enter the total cost of gas for day {value + 1}: ')))
    total_food = sum(food)  # sum function allows you to get the contents of a list added together
    total_gas = sum(gas)
    total_cost = total_food + total_gas
    person_cost = total_cost / people
    print('The total cost of food is: ', total_food)
    print('The total cost of gas is: ', total_gas)
    print('The total cost of the trip is: ', total_cost)
    print('The cost per person is: ', person_cost)


if __name__ == '__main__':
    main()
