import math


def firstrun():
    return "success"


def areaofcircle(radius):
    if(type(radius) is not (int or float)):
        return "Enter a float or int for the radius."
    elif(radius <= 0):
        return "Enter a positive number for the radius."
    else:
        return math.pi * radius * radius
