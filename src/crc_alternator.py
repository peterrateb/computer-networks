"""
Inverts 1 bit on the first line
depending on its argument (the bit number counting the leftmost bit
as 1) but copies the rest of the two lines correctly.
"""


from __crc_helpers import string_to_bool_list, bool_list_to_string
from sys import argv, stdin, exit


def alternate(data, bit_no):
    """
    Arguments:
    data -- input data (a list of bool values that represent the data) also known as D
    bit_no -- bit to be inverted (a bit number that must be <= len(data) to be inverted in the data)
    
    Returns:
    data_inverted -- output data (a list of bool values that represent the data with the required bit inverted)
    """

    if bit_no > len(data) or bit_no <= 0:
        raise Exception('Incorrect bit to invert.')
    data[bit_no - 1] = int(not data[bit_no - 1])
    return data


if __name__ == '__main__':
    """
    Arguments:
    bit to be inverted
    (m+k) 0s and 1s representing the message
    the generator polynomial
    
    Prints:
    (m+k) 0s and 1s representing the message to be transmitted with the required bit inverted
    the generator polynomial just as recieved
    """
    
    if '-h' in argv:
        exit('`alternate bit_no`')
    if len(argv) != 2:
        raise Exception('You didn\'t complete the input.')
    
    arg = []
    for line in stdin:
        arg.append(line)
    transmitted_data, polynomial = string_to_bool_list(arg[0]), arg[1]
    
    alternate(transmitted_data, int(argv[1]))
    print(bool_list_to_string(transmitted_data), polynomial, sep='\n')
