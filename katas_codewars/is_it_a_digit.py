# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.


def is_digit(n):
    n = str(n)
    is_digit_n = n.isdigit()
    if is_digit_n is True and len(n) == 1:
        return True
    else:
        return False


# def is_digit(n):
    # return n.isdigit() and len(n)==1


# def is_digit(n):
    # try: 
        # if int(n) < 10 > 0 and len(n) == 1:
            # return True
        # else:
            # return False
    # except:
        # return Falses