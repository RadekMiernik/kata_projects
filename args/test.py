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

