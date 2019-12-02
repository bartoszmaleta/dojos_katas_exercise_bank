# You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.

array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]

# print(array)
# # sorted(array)
# new_array = array.sort()
# print(array)


def two_sort(array):
    print(array)
    array.sort()
    print(array)

    first_elem = array[0]
    print(first_elem)
    result = ''
    for elem in first_elem:
        result += elem
        result += "***"
    print(result)
    len_ = len(result)
    true_len = len_ - 3
    result = result[:true_len]
    print(result[:true_len])
    return result


two_sort(array)