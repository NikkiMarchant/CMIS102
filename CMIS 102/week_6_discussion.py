#  Nicole Marchant CMIS 102 6980 Week 6 Discussion
# Swaps upper and lower case letters and looks for initials.

def main():
    sen = input('Write a sentence:')
    new_sen = ''
    for letters in sen:
        new_sen += letters.swapcase()  # appending charter to new_sen string
    print(new_sen)
    if 'nm' in sen.lower():  # checking to see if initials are in the string
        print('Initials found')


if __name__ == '__main__':
    main()
