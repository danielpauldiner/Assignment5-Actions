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


def firstlastlist(enterdlist):
    if(type(enterdlist) is not list):
        return "Enter a list."
    elif(enterdlist == []):
        return "Enter a list that isn't empty"
    else:
        return [enterdlist[0], enterdlist[-1]]
