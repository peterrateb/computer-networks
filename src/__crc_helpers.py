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
    bool_list = []
    for char in string:
        if char == '1':
            bool_list.append(1)
        else:
            bool_list.append(0)

    return bool_list


def xor(A, B):
    """
        Arguments:
        A,B two strings of zeros and ones with same length

        Returns:
        result -- a string of zeros and ones contains the xor result of A and B
    """
    result = ""
    for i in range(len(A)):
        if A[i] != B[i]:
            result += "1"
        else:
            result += "0"
    return result


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
    polynomial_length = len(polynomial)
    polynomial_order = polynomial_length - 1
    index = 0
    pick = ""
    while index < len(data):
        if len(pick) != polynomial_length:
            pick += str(data[index])
            index += 1
        else:
            if pick[0] == '0':
                pick = pick[1:]
                pick += str(data[index])
                index += 1
                continue
            pick = xor(string_to_bool(pick), polynomial)
    if len(pick) == polynomial_length:
        pick = xor(string_to_bool(pick), polynomial)
    return pick[len(pick)-polynomial_order:]


def print_bool_list(bool_list):
    """
    bool_list -- a list of bool values, ex: [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

    Prints:
    a string of the bool_list values concatinated, ex: 0110101001
    """
    str = ""
    for boolean in bool_list:
        if boolean:
            str += "1"
        else:
            str += "0"

    print(str)


if __name__ == '__main__':

    print(divide([1, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1]))
    # raise Exception('YOU CANT CALL THIS CODE')
