from colorama import Fore, Style, Back

# dictionary of possibles other numbers than original
dict_possible = {1: (7,), 2: (6,), 3: (9,), 4: (), 5: (9, 6), 6: (5, 8), 7: (1,), 8: (0, 6, 9),
                 9: (3, 5, 8), 0: (8,)}

# validated numbers when scanned line by line from example
# 0 from scanner is:
#
#  _
# | |
# |_|
# so num_0_val = [' ', '_', ' ', '|', ' ', '|', '|', '_', '|'] is a representation of 0
num_0_val = [' ', '_', ' ', '|', ' ', '|', '|', '_', '|']  # 0
num_1_val = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|']  # 1
num_2_val = [' ', '_', ' ', ' ', '_', '|', '|', '_', ' ']  # 2
num_3_val = [' ', '_', ' ', ' ', '_', '|', ' ', '_', '|']  # 3
num_4_val = [' ', ' ', ' ', '|', '_', '|', ' ', ' ', '|']  # 4
num_5_val = [' ', '_', ' ', '|', '_', ' ', ' ', '_', '|']  # 5
num_6_val = [' ', '_', ' ', '|', '_', ' ', '|', '_', '|']  # 6
num_7_val = [' ', '_', ' ', ' ', ' ', '|', ' ', ' ', '|']  # 7
num_8_val = [' ', '_', ' ', '|', '_', '|', '|', '_', '|']  # 8
num_9_val = [' ', '_', ' ', '|', '_', '|', ' ', '_', '|']  # 9
num_val_list = [num_0_val, num_1_val, num_2_val, num_3_val, num_4_val,
                num_5_val, num_6_val, num_7_val, num_8_val, num_9_val]


def check_account(account_given: str):
    """Simple function which checks if given account is valid

    Arguments:
        account_given (str): str form of digit version of account

    Returns:
        '{}{}{}{}'.format(Fore.GREEN, Back.LIGHTBLACK_EX, 'VALID', Style.RESET_ALL)
            - account is valid
        '{}{}{}{}'.format(Fore.BLACK, Back.LIGHTRED_EX, 'ERR', Style.RESET_ALL)
            - account is not valid
        '{}{}{}{}'.format(Fore.BLACK, Back.LIGHTYELLOW_EX, 'ILL', Style.RESET_ALL)
            - there are some additional or missed lines in code from scanner
    """
    x = account_given
    j = 9
    checksum = 0
    try:
        for _ in x:
            checksum += j*int(_)
            j -= 1
        if checksum % 11 == 0:
            return '{}{}{}{}'.format(Fore.GREEN, Back.LIGHTBLACK_EX, 'VALID', Style.RESET_ALL)
        else:
            return '{}{}{}{}'.format(Fore.BLACK, Back.LIGHTRED_EX, 'ERR', Style.RESET_ALL)
    except ValueError:
        return '{}{}{}{}'.format(Fore.BLACK, Back.LIGHTYELLOW_EX, 'ILL', Style.RESET_ALL)


def check_possibilities(account_nr_to_check: str):  # TODO: actualize the docstring (returns) and ? problems
    """Checking other possibilities if scanned data is not valid (ERR or ILL).

    Arguments:
        account_nr_to_check (str): string version of account

    Returns:
        lists: other valid possibilities of account number
    """
    others = []
    if check_account(account_nr_to_check) == '{}{}{}{}'.format(Fore.BLACK, Back.LIGHTRED_EX, 'ERR', Style.RESET_ALL) or \
            check_account(account_nr_to_check) == '{}{}{}{}'.format(
            Fore.BLACK, Back.LIGHTYELLOW_EX, 'ILL', Style.RESET_ALL):
        i = 0
        while i < 10:
            for char in account_nr_to_check:
                for _ in '1234567890':
                    try:
                        if int(_) in dict_possible.get(int(char)):
                            if i == 0:
                                other = _ + account_nr_to_check[i + 1:]
                                valid = check_account(other)
                                if valid == '{}{}{}{}'.format(Fore.GREEN, Back.LIGHTBLACK_EX, 'VALID', Style.RESET_ALL)\
                                        and other not in others:
                                    others.append(other)
                            elif 1 <= i < 9:
                                other = account_nr_to_check[:i] + _ + account_nr_to_check[i + 1:]
                                valid = check_account(other)
                                if valid == '{}{}{}{}'.format(Fore.GREEN, Back.LIGHTBLACK_EX, 'VALID', Style.RESET_ALL)\
                                        and other not in others:
                                    others.append(other)
                    except ValueError:  # TODO: tutaj trzeba dodać validację źle odczytanego znaku, który daje ?
                        pass
                i += 1
    else:
        print('Here you have to add sth to deal with ?')
    if len(others) == 1:
        return 'Account nr: {}'.format(others[0])
    elif len(others) > 1:
        return 'AMB {}'.format(others)
    else:
        return 'No other possibilities'


def lines_on_numbers(given_example: str, valid_list_of_numbers=None):
    """Changing tuple of lists with characters into readable form of account number.

    Arguments:
        given_example (str): data from scanner
        valid_list_of_numbers (list): list of valid numbers build from sequences of characters which are needed for each
                                      character

    Returns:
        str: account number in readable simple form
    """
    given_account = reading(given_example)
    if valid_list_of_numbers is None:
        valid_list_of_numbers = num_val_list
    account_checked = ''
    invalid_char = []
    for num_ac in given_account:
        if num_ac in valid_list_of_numbers:
            for num_val in valid_list_of_numbers:
                if num_ac == num_val:
                    account_checked += str(valid_list_of_numbers.index(num_val))
        else:
            account_checked += '?'
            invalid_char += num_ac
    return account_checked, invalid_char


def reading(given_example: str):
    """Returns a lists (with 9 elements) (in one tuple) of characters of each number in scanned data.

    Arguments:
        given_example (str): data from scanner

    Returns:
        tuple with 9 elements - each element is a list with 9 characters taken from data after scanning.
    """
    num_1 = []
    num_2 = []
    num_3 = []
    num_4 = []
    num_5 = []
    num_6 = []
    num_7 = []
    num_8 = []
    num_9 = []
    final_account = (num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9)
    i = 28
    for _ in given_example[28:]:
        if _ == '\n':
            pass
            i += 1
        else:
            if 28 <= i <= 30 or 56 <= i <= 58 or 84 <= i <= 86:
                num_1.append(_)
            elif 31 <= i <= 33 or 59 <= i <= 61 or 87 <= i <= 89:
                num_2.append(_)
            elif 34 <= i <= 36 or 62 <= i <= 64 or 90 <= i <= 92:
                num_3.append(_)
            elif 37 <= i <= 39 or 65 <= i <= 67 or 93 <= i <= 95:
                num_4.append(_)
            elif 40 <= i <= 42 or 68 <= i <= 70 or 96 <= i <= 98:
                num_5.append(_)
            elif 43 <= i <= 45 or 71 <= i <= 73 or 99 <= i <= 101:
                num_6.append(_)
            elif 46 <= i <= 48 or 74 <= i <= 76 or 102 <= i <= 104:
                num_7.append(_)
            elif 49 <= i <= 51 or 77 <= i <= 79 or 105 <= i <= 107:
                num_8.append(_)
            elif 52 <= i <= 54 or 80 <= i <= 82 or 108 <= i <= 110:
                num_9.append(_)
            i += 1
    return final_account


def printing_details(account_nr: str):
    """Simple function needed to print all data about account in one step"""

    statement = 'Data from scanner: {}\nData status: {}\nOther possibilities: {}'.format(
        account_nr, check_account(account_nr), check_possibilities(account_nr))
    print(statement)


example = '''\
                           
    _  _     _  _  _  _  _ 
 _| _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|'''


if __name__ == '__main__':
    # account = lines_on_numbers(example)
    # cos_tam = lines_on_numbers(example)
    # print(account)
    # printing_details(account[0])
    # print(lines_on_numbers(account, num_val_list))

    # checking_account = '666666666'
    #
    # print(check_possibilities(checking_account))

    # i = 0  # TODO: z tego musisz wykombinować jak zrobić coś takiego, że jak się dwa tylko jeden znak różni - daje jako możliwość
    # x = 0
    # while i < 10:
    #     print(x)
    #     for char in num_val_list[x]:
    #         print(char, end='')
    #     x += 1
    #     print('***')
    #     i += 1

    num_check = [' ', ' ', ' ', ' ', '_', '|', ' ', ' ', '|']
    num_4_val = [' ', ' ', ' ', '|', '_', '|', ' ', ' ', '|']

    def difference (list1, list2):
        diff = []
        for char in list1:
            for _ in list2:
                wrong = 0
                for sign in _:
                    if char == sign:
                        pass
                    elif wrong >= 2:
                        break
                    else:
                        wrong += 1
                        if wrong < 2:
                            diff += str(list2.index(_))
        return set(diff)

    y = difference(num_check, num_val_list)
    print(y)


