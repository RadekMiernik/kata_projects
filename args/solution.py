# this task is from https://codingdojo.org/kata/Args/


def returning_values():
    statement = '-l'  # input('Please input your command line:\n')
    error_msg = 'Sorry but your command is wrong'                     # TODO: those variables should be at the end

    flags = {'-l': ['LOG', False, None], '-p': ['PORT', 0, None], '-d': ['DIR', '', None],
             '-g': ['LIST OF STR', [], None], '-m': ['LIST OF INT', [], None]}
    used_flags = []
    for _ in flags.keys():
        if _ in statement:
            flags[_][2] = statement.index(_)
            used_flags.append(_)
    for _ in used_flags:
        if len(used_flags) == 1:
            print('{}: {}'.format(flags[_][0], flags[_][1]))
    print(len(used_flags))
    print(flags)
    print(used_flags)
    print(flags['-g'][2] != None)

    log = flags['-l'][1]
    port = flags['-p'][1]
    directory = flags['-d'][1]
    list_of_str = flags['-g'][1]
    list_of_int = flags['-m'][1]
    final_statement = 'Log: {}\nPort: {}\nDirectory: {}\nList of str: {}\nList of int: {}'.format(
        log, port, directory, list_of_str, list_of_int)

    # or
    print('**' * 20)
    for _ in flags.keys():
        print('{}: {}'.format(flags[_][0], flags[_][1]))
    print('**' * 20)

    # return final_statement



print(returning_values())
