"""
Helper functions to be used in other files
"""


def string_to_bool_list(string):
    """
    Arguments:
    string -- input data as a string of zeros and ones, ex: 0110101001

    Returns:
    bool_list -- a list of bool values that is equivalent to the input string, ex: [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    """
    
    bool_list = []
    for char in string:
        if char == '0':
            bool_list.append(0)
        elif char == '1':
            bool_list.append(1)

    return bool_list


def xor(a, b):
    """
    Arguments:
    a, b -- Two bool lists with the same length

    Returns:
    result -- A bool list containing the result of the xor
    """
    
    result = []
    for i in range(len(a)):
        result.append(int(a[i] != b[i]))
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
    
    data_copy = data.copy()
    data_length = len(data_copy)
    polynomial_length = len(polynomial)
    polynomial_order = polynomial_length - 1
    for div_no in range(data_length - polynomial_length + 1):
        div_data = data_copy[div_no : div_no + polynomial_length]
        if div_data[0] == 0:
            continue
        data_copy[div_no : div_no+polynomial_length] = xor(div_data, polynomial)
    return data_copy[data_length - polynomial_length + 1:]


def bool_list_to_string(bool_list):
    """
    bool_list -- a list of bool values, ex: [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

    Prints:
    a string of the bool_list values concatinated, ex: 0110101001
    """
    
    string = ""
    for boolean in bool_list:
        string += str(boolean)
    return(string)


if __name__ == '__main__':
    raise Exception('YOU CANT CALL THIS CODE')
