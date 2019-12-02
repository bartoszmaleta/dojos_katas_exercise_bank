# Your task is to add up letters to one letter.

# The function will be given a variable amount of arguments, each one being a letter to add.

# Notes:
# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
# Examples:
# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'


def add_letters(*letters):
# def add_letters(letter):
    # your code here
    list_with_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_of_letters = 'abcdefghijklmnopqrstuvwxyz'
    print(list_with_letters)

    list_with_numbers = []
    for index in range(len(list_with_letters)):
        list_with_numbers.append(index + 1)

    print(list_with_numbers)

    answer_list = []
    if letters in string_of_letters:
        answer_list.append(letters)

    print(answer_list)
    first_elem_of_answer_list = answer_list[0]
    print(list_with_letters.index(first_elem_of_answer_list) + 1)


add_letters("a", "b")