# Nicole Marchant CMIS 102 6980
# Compute cost of house cleaning based on number of rooms and type of cleaning.

def main():
    room_num = eval(input('Number of Rooms:'))
    # used https://www.geeksforgeeks.org/python-string-lower/# to learn the .lower method
    cleaning_type = input('Choose General, Deep, or Garage cleaning:').lower()
    house_size = 0
    # used https://www.geeksforgeeks.org/python-dictionary/ to properly utilize dictionaries
    cleaning_dict = {'general': 1, 'deep': 2, 'garage': .8}
    house_dict = {'small': 100, 'medium': 200, 'large': 300}

    if room_num < 5:  # chose a standard 2 bedroom 1-bath house as cut off
        house_size = house_dict.get('small')
    elif room_num > 7:  # anything over a 3 bedroom 2-bath house
        house_size = house_dict.get('large')
    else:
        house_size = house_dict.get('medium')  # chose a 3 bedroom 2-bath house as cut off

    cost = (((1+(room_num * .1))*house_size)*cleaning_dict.get(cleaning_type))
    print('Cost:', round(cost, 2))  # rounded answer to second decimal point

    return


main()
