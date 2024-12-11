#  Nicole Marchant CMIS 102/6980
#  Prompts user to enter 5 anime titles and the number of episodes
#  Sorts the titles alphabetically and then by number of episodes.
import random
# https://www.geeksforgeeks.org/python-scramble-strings-in-list/# used for the shuffle


def main():
    anime = []
    print("List five anime titles to be scrambled.")
    for value in range(5):  # loop five times
        anime.append(input("Please input anime title: "))
    for value in range(len(anime)):
        scramble = list(anime[value])  # shuffle needs a mutable type
        random.shuffle(scramble)
        anime[value] = ''.join(scramble)
    print('Here are the scrambled titles of the anime entered:')
    for value in range(len(anime)):
        print(anime[value])


if __name__ == '__main__':
    main()
