"""
The verifier program reads in the output of the generator program and
outputs a message indicating whether it is correct or not.
"""


from __crc_helpers import string_to_bool, divide, print_bool_list 


def verify(data, polynomial, remainder):
    """
    Arguments:
    data -- input data (a list of bool values that represent the data) also known as D
    polynomial -- generator polynomial (a list of bool values that represent the values of different coefficients of the polynomial) also known as G
    remainder -- the remainder of the division also known as R

    Returns:
    error_detected -- boolen value to indicate whether there is some error in the recieved data

    Hints:
    polynomial_order = len(polynomial) - 1
    """

    pass


if __name__ == '__main__':
    """
    Arguments:
    (m+k) 0s and 1s representing the message
    the generator polynomial

    Prints:
    A message indicating whether the input is correct or not
    """

    pass
