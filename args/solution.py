# this task is from https://codingdojo.org/kata/Args/

command = '-l -p 8080 -d /usr/logs'
list_of_data = command.split(' ')
log_info = False
port_info = 0
dir_info = ''
print(list_of_data)
try:
    if '-l' in list_of_data:
        log_info = True
        if not list_of_data[(list_of_data.index('-l') + 1)].startswith('-'):
            print('You added unnecessary value \'{}\' after -l: we ignored it.'.format(
                list_of_data[(list_of_data.index('-l') + 1)]))
    if '-p' in list_of_data:
        port_info = list_of_data[(list_of_data.index('-p') + 1)]
        try:
            port_info = int(port_info)
        except ValueError:
            port_info = 'Port can be only a number'
    if '-d' in list_of_data:
        dir_info = list_of_data[(list_of_data.index('-d') + 1)]
        if len(dir_info) == 0:
            dir_info = 'You passed too many spaces between -d and the path'
except ValueError:
    print('Remember about proper syntax')
print(log_info)
print(port_info)
print(dir_info)
