# Nicole Marchant CMIS 102 6980
# Compute cost of house cleaning or yard work.

def cleaning_price(room_num: int, cleaning_type: str):
    cleaning_dict = {'general': 1, 'deep': 2, 'garage': .8}
    house_dict = {'small': 100, 'medium': 200, 'large': 300}

    if room_num < 5:  # chose a standard 2 bedroom 1-bath house as cut off
        house_size = house_dict.get('small')
    elif room_num > 7:  # anything over a 3 bedroom 2-bath house
        house_size = house_dict.get('large')
    else:
        house_size = house_dict.get('medium')  # chose a 3 bedroom 2-bath house as cut off

    cost = (((1+(room_num * .1))*house_size)*cleaning_dict.get(cleaning_type))
    return cost


def cleaning_menu():
    room_num = eval(input('Number of Rooms: '))
    cleaning_type = input('Choose General, Deep, or Garage cleaning: ').lower()
    house_size = 0
    cost = cleaning_price(room_num, cleaning_type)
    return cost


def yard_cost(mowing, edging, shrubs):
    # The cost of the mowing depends upon the square footage of the yard, the cost of edging depends upon the linear
    # footage of the yard's edges, and the cost of shrub pruning depends upon the number of shrubs.
    mowing_cost = 20 * mowing
    edging_cost = 5 * edging
    shrub_cost = 10 * shrubs
    cost = mowing_cost + edging_cost + shrub_cost
    return cost


def yard_menu():
    # Yard service involves mowing, edging, and shrub pruning
    mowing = eval(input('Square feet of yard for mowing: '))
    edging = eval(input('Feet of yard for edging: '))
    shrub = eval(input('Number of shrubs: '))
    cost = yard_cost(mowing, edging, shrub)
    return cost


def main():
    cost = 0
    while True:
        job_input = input('Yard work or House Cleaning: ')
        if job_input.lower() == "yard work" or job_input.lower() == 'house cleaning':
            break
        else:
            print("Invalid input")

    discount_input = input('Are you over 65 years old? ')

    if job_input.lower() == "yard work":
        cost = yard_menu()
    elif job_input.lower() == "house cleaning":
        cost = cleaning_menu()

    if discount_input.lower() == 'yes':
        cost *= .9
    print('Cost: ', round(cost, 2))  # rounded answer to second decimal point


if __name__ == '__main__':
    main()


