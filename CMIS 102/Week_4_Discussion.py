# Nicole Marchant CMIS 102 6980
# calculates the volume of a cone given radius and height
import math

def cone_volume(r=0, h=0):
    v = 1/3*(math.pi*(r**2)*h)
    return v


def main():
    print('Finding the volume of a cone')
    radius = eval(input('Please enter the radius '))
    height = eval(input('Please enter the height '))
    volume = cone_volume(radius, height)
    print('Your cones volume is', volume)


if __name__ == '__main__':
    main()
