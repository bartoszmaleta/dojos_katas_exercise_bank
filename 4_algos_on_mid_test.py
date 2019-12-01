

def get_common_elements(first_list, second_list):
    """
    Function should return a list containing elements that are on both input lists.

    >>> get_common_elements([1, 2, 3], [3, 4, 5])
    [3]

    >>> get_common_elements([3, 5, 8], [3, 4, 5, 12, 8])
    [3, 5, 8]

    """
    list_with_numbers_on_both_list = []
    for elem in first_list:
        if elem in second_list:
            list_with_numbers_on_both_list.append(elem)
    
    # print(list_with_numbers_on_both_list)
    return list_with_numbers_on_both_list


# first_list_with_numbers = [3, 5, 8]
# second_list_with_numbers = [3, 4, 5, 12, 8]
# get_common_elements(first_list_with_numbers, second_list_with_numbers)
# ---------------------------------------------------------------


def get_odd_elements(x, start):
    """
    Function should return a list containing first 'x' odd elements,
    starting from 'start' value.

    >>> get_odd_elements(2, 31)
    [31, 33]

    >>> get_odd_elements(3, 10)
    [11, 13, 15]
    """


# ---------------------------------------------------------------


def get_sum_of_all_even_elements(my_list):
    """
    Function should sum all it's even elements and return it as an integer.

    >>> get_sum_of_all_even_elements([1, 15, 21])
    0

    >>> get_sum_of_all_even_elements([1, 2, 3, 6, 9, 11])
    8

    """
    sum_of_all_even_elements = 0
    for elem in my_list:
        if elem % 2 == 0:
            sum_of_all_even_elements += elem

    return sum_of_all_even_elements


# ---------------------------------------------------------------


def get_letters_statistics(word):
    """
    Function should return a dictionary where keys are letters and coresponding values are quantities of that letters.

    >>> result = get_letters_statistics('abc')
    >>> result == {'a': 1, 'b': 1, 'c': 1}
    True

    >>> result2 = get_letters_statistics('abrakadabra')
    >>> result2 == {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}
    True

    """


# ---------------------------------------------------------------

