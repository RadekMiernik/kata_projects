# class FlagDefinition:
#
#     def __init__(self, name, type_expected):
#         pass
#
#


def parse(command, flags):
    return 'x'


def test_parse_params():
    flags = [("-l", bool), ("-p", int), ("-d", str)]

    result = parse(command="-l -p 8080 -d /usr/logs", flags=flags)

    assert result == {("-d", True), ("-p", 8080), ("-d", "/usr/logs")}


# def test_parse_params():
#     log_flag = FlagDefinition(name="-l", type_expected=bool)
#     port_flag = FlagDefinition(name="-p", type_expected=int)
#     dst_flag = FlagDefinition(name="-d", type_expected=str)
#     flags = [log_flag, port_flag, dst_flag]
#
#     result = parse(command="-l -p 8080 -d /usr/logs", flags=flags)
#
#     assert result == {
#         FlagValue(flag=log_flag, value=True),
#         FlagValue(flag=port_flag, value=8080),
#         FlagValue(flag=dst_flag, value="/usr/logs"),
#     }


# def test_parse_params():
#     log_flag = FlagDefinition(name="-l", type=bool)
#     port_flag = FlagDefinition(name="-p", type=int)
#     dst_flag = FlagDefinition(name="-d", type=str)
#     flags = [log_flag, port_flag, dst_flag]
#
#     result = parse(input="-l -p 8080 -d /usr/logs", flags=flags)


# class Flag:
#
#     def __init__(self, flag: str, expected_type):
#         self.flag = flag
#         self.expected_type = expected_type
#
#     def result(self, statement):
#         pass
# #

#
# def returning_values():
#     statement = '-l'  # input('Please input your command line:\n')
#     error_msg = 'Sorry but your command is wrong'                     # TODO: those variables should be at the end
#
#     flags = {'-l': ['LOG', False, None], '-p': ['PORT', 0, None], '-d': ['DIR', '', None],
#              '-g': ['LIST OF STR', [], None], '-m': ['LIST OF INT', [], None]}
#     used_flags = []
#     for _ in flags.keys():
#         if _ in statement:
#             flags[_][2] = statement.index(_)
#             used_flags.append(_)
#     for _ in used_flags:
#         if len(used_flags) == 1:
#             print('{}: {}'.format(flags[_][0], flags[_][1]))
#     print(len(used_flags))
#     print(flags)
#     print(used_flags)
#     print(flags['-g'][2] != None)
#
#     log = flags['-l'][1]
#     port = flags['-p'][1]
#     directory = flags['-d'][1]
#     list_of_str = flags['-g'][1]
#     list_of_int = flags['-m'][1]
#     final_statement = 'Log: {}\nPort: {}\nDirectory: {}\nList of str: {}\nList of int: {}'.format(
#         log, port, directory, list_of_str, list_of_int)
#
#     # or
#     print('**' * 20)
#     for _ in flags.keys():
#         print('{}: {}'.format(flags[_][0], flags[_][1]))
#     print('**' * 20)
#
#     # return final_statement
#
#
#
# print(returning_values())
