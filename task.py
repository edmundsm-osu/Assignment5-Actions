import math


def firstrun():
    return "success"


def calc_area(radius):
    return math.pi * (radius * radius)


def first_last(collection):
    if len(collection) == 0:
        return []

    to_return = []
    # add first element
    to_return.append(collection[0])
    # add last element
    to_return.append(collection[-1])
    return to_return


# Source: https://docs.python.org/2/library/datetime.html
def days_between(first_date, second_date):
    to_return = second_date - first_date
    return abs(to_return.days)
