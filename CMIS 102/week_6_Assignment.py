# Nicole Marchant CMIS 102 6980 July 24th 2023
# This program checks to see if a users password is valid and if not tells them why.

def pass_length(password):
    # pass_length checks if the password is between 8 and 16 characters
    min_length = 8
    max_length = 16

    if max_length >= len(password) >= min_length:
        return True  # return True if password length is between the min and max values
    return False


def chara_dig(password):
    # chara_dig checks if the password contains an alpha and a digit
    alpha = False
    digit = False
    for character in password:
        if character.isalpha():
            alpha = True
        if character.isdigit():
            digit = True
    if alpha and digit:
        return True  # return True if password contains an alpha and a digit
    return False


def forbidden(password):
    # forbidden checks if the password contains the forbidden space character
    if ' ' not in password:
        return True  # return True if there are no space characters in the password
    return False


def main():
    print('Secure password must be 8-16 characters, include at least one letter and one number, and contain no spaces')
    user_input = input('Please enter your password:')
    check = pass_length(user_input)
    if not check:  # if check is False, invalid length
        print('Invalid character length')
        return
    # verify check
    check = chara_dig(user_input)
    if not check:  # if check is False, missing digit or alpha
        print('Password must have one digit and one alphabetic character')
        return
    check = forbidden(user_input)
    if not check:  # if check is False, space in password
        print('Password must not contain any spaces')
        return

    print('Password was Accepted')


if __name__ == '__main__':
    main()
