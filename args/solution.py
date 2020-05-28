# this task is from https://codingdojo.org/kata/Args/

# command = '-l -p 8080 -d /url/sth'


def parse(statement):
    list_of_data = statement.split(' ')
    log_info = False
    port_info = 0
    dir_info = ''
    try:
        if '-l' in list_of_data and list_of_data[(list_of_data.index('-l'))].endswith('l'):
            log_info = True
            if not list_of_data[(list_of_data.index('-l') + 1)].startswith('-'):
                print('You added unnecessary value \'{}\' after -l: we ignored it.'.format(
                    list_of_data[(list_of_data.index('-l') + 1)]))
        if '-p' in list_of_data:
            port_info = list_of_data[(list_of_data.index('-p') + 1)]
            try:
                port_info = int(port_info)
            except ValueError:
                if len(list_of_data[(list_of_data.index('-p') + 1)]) == 0:
                    print('It looks like you added too many spaces between flag -p and port number')
                    port_info = 0
                else:
                    port_info = 'Port can be only a number, you used \'{}\''.format(
                        list_of_data[(list_of_data.index('-p') + 1)])
        if '-d' in list_of_data:
            try:
                if len(list_of_data[(list_of_data.index('-d') + 1)]) == 0:
                    print('You passed too many spaces between -d and the path')
                else:
                    dir_info = list_of_data[(list_of_data.index('-d') + 1)]
            except IndexError:
                print('You did not put any value after -d flag')
    except ValueError:
        print('Remember about proper syntax')

    print('LOG: {}\nPORT: {}\nDIR: {}'.format(log_info, port_info, dir_info))


if __name__ == '__main__':
    x = input('Please input a command: ')
    parse(x)
    