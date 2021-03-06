"""
The generator program reads from standard input a line of ASCII text
containing an m-bit message consisting of a string of 0s and 1s. The
second line is the k-bits polynomial, also in ASCII. It outputs to
standard output a line of ASCII text with (m+k) 0s and 1s representing
the message to be transmitted. Then it outputs the polynomial, just as
it read it in.
"""


from __crc_helpers import string_to_bool_list, divide, bool_list_to_string
from sys import stdin, exit


def generator(data, polynomial):
    """
    Arguments:
    data -- input data (a list of bool values that represent the data) also known as D
    polynomial -- generator polynomial (a list of bool values that represent the values of different coefficients of the polynomial) also known as G
    
    Returns:
    message -- the message to be transmitted (a list of bool values that represent the D+R bits in the output message)
    
    Hints:
    polynomial_order = len(polynomial) - 1
    """
    
    remainder = divide(data + [0] * (len(polynomial) - 1), polynomial)
    message = data + remainder
    return message


if __name__ == '__main__':
    """
    Arguments:
    (m) 0s and 1s representing the message
    the generator polynomial
    
    Prints:
    (m+k) 0s and 1s representing the message to be transmitted
    the generator polynomial just as recieved
    """

    arg = []
    for line in stdin:
        arg.append(line)
    data, polynomial = string_to_bool_list(arg[0]), string_to_bool_list(arg[1])
    
    message = bool_list_to_string(generator(data, polynomial))
    out = open('transmitted_message.txt', 'w')
    out.write(message)
    out.close()
    print(message, arg[1], sep='\n')
