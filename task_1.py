
dict_possible = {1: (7,), 2: (6,), 3: (9,), 4: (), 5: (9, 6), 6: (5, 8), 7: (1,), 8: (0, 6, 9),
                 9: (3, 5, 8), 0: (8,)}

num_0_val = [' ', '_', ' ', '|', ' ', '|', '|', '_', '|']
num_1_val = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|']
num_2_val = [' ', '_', ' ', ' ', '_', '|', '|', '_', ' ']
num_3_val = [' ', '_', ' ', ' ', '_', '|', ' ', '_', '|']
num_4_val = [' ', ' ', ' ', '|', '_', '|', ' ', ' ', '|']
num_5_val = [' ', '_', ' ', '|', '_', ' ', ' ', '_', '|']
num_6_val = [' ', '_', ' ', '|', '_', ' ', '|', '_', '|']
num_7_val = [' ', '_', ' ', ' ', ' ', '|', ' ', ' ', '|']
num_8_val = [' ', '_', ' ', '|', '_', '|', '|', '_', '|']
num_9_val = [' ', '_', ' ', '|', '_', '|', ' ', '_', '|']
num_val_list = [num_0_val, num_1_val, num_2_val, num_3_val, num_4_val,
                num_5_val, num_6_val, num_7_val, num_8_val, num_9_val]

numbers = '1234567890'


def check_account(account_given):
    x = account_given
    j = 9
    checksum = 0
    try:
        for _ in x:
            checksum += j*int(_)
            j -= 1
        if checksum % 11 == 0:
            return ' VALID'
        else:
            return ' ERR'
    except ValueError:
        return ' ILL'


def check_possibilities(checking_account):
    others = []
    if check_account(checking_account) == ' ERR':
        i = 0
        while i < 10:
            for char in check:
                for _ in numbers:
                    if int(_) in dict_possible.get(int(char)):
                        if i == 0:
                            other = _ + check[i+1:]
                            valid = check_account(other)
                            if valid == ' VALID' and other not in others:
                                others.append(other)
                        if 1 <= i < 9:
                            other = check[:i] + _ + check[i+1:]
                            valid = check_account(other)
                            if valid == ' VALID' and other not in others:
                                others.append(other)
                        else:
                            pass
                i += 1
    else:
        print('Here you have to add sth to deal with ?')
    return others


def lines_on_numbers(given_account, valid_list_of_numbers=num_val_list):
    account_checked = ''
    for num_ac in given_account:
        if num_ac in valid_list_of_numbers:
            for num_val in valid_list_of_numbers:
                if num_ac == num_val:
                    account_checked += str(valid_list_of_numbers.index(num_val))
        else:
            account_checked += '?'
    return account_checked


def reading(given_example):
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


example = '''\
                           
 _     _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |'''


account = reading(example)
print(lines_on_numbers(account, num_val_list))

print(check_account('490068715'))

check = '0?0000051'

print(check_possibilities(check))
