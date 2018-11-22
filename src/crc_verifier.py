"""
The verifier program reads in the output of the generator program and
outputs a message indicating whether it is correct or not.
"""


from __crc_helpers import string_to_bool_list, divide, bool_list_to_string
from sys import stdin, exit


def verify(data, polynomial):
    """
    Arguments:
    data -- input data (a list of bool values that represent the data) also known as D
    polynomial -- generator polynomial (a list of bool values that represent the values of different coefficients of the polynomial) also known as G
    
    Returns:
    correct_data -- boolen value to indicate whether there is some error in the recieved data
    
    Hints:
    polynomial_order = len(polynomial) - 1
    """
    
    verifier_remainder = divide(data, polynomial)
    if 1 in verifier_remainder:
        return False
    return True


if __name__ == '__main__':
    """
    Arguments:
    (m+k) 0s and 1s representing the message
    the generator polynomial
    
    Prints:
    A message indicating whether the input is correct or not
    """
    
    arg = []
    for line in stdin:
        arg.append(line)
    transmitted_data, polynomial = string_to_bool_list(arg[0]), string_to_bool_list(arg[1])
    
    if verify(transmitted_data, polynomial):
        print('Correct data transmission')
    else:
        print('Incorrect data transmission')
