"""
Helper functions to be used in other files
"""


def string_to_bool(string):
    """
    Arguments:
    string -- input data as a string of zeros and ones, ex: 0110101001

    Returns:
    bool_list -- a list of bool values that is equivalent to the input string, ex: [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    """

    pass

def divide(data, polynomial):
    """
    Arguments:
    data -- input data (a list of bool values that represent the data) also known as D
    polynomial -- generator polynomial (a list of bool values that represent the values of different coefficients of the polynomial) also known as G

    Returns:
    remainder -- the remainder of the division also known as R

    Hints:
    polynomial_order = len(polynomial) - 1
    """

    pass

def print_bool_list(bool_list):
    """
    bool_list -- a list of bool values, ex: [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

    Prints:
    a string of the bool_list values concatinated, ex: 0110101001
    """

    pass


if __name__ == '__main__':
    raise Exception('YOU CANT CALL THIS CODE')
