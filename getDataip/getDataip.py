import ClassDatasetIP
import sys

args = sys.argv
datasetIP = ClassDatasetIP.DatasetIP()
n = '-n'

try:
    if args[1] == '0':
            print(datasetIP.get_external_ipv4())
    elif args[1] == '1':
        if args[2] == n:
            ip = None
        else:
            ip = args[2]
        if args[3] == n:
            countdown = 10
        else:
            countdown = args[3]
        print(datasetIP.get_dataset_without_api(ip, countdown))
    elif args[1] == '2':
        if args[4] == n:
            ip = None
        else:
            ip = args[4]
        if args[5] == n:
            hostname = None
        else:
            hostname = args[5]
        if args[6] == n:
            time_zone = None
        else:
            time_zone = args[6]
        if args[7] == n:
            currency = None
        else:
            currency = args[7]
        if args[8] == n:
            security = None
        else:
            security = args[8]
        count, dict_elements = datasetIP.get_dataset_with_api(args[2], args[3], ip, hostname, time_zone, currency, security)
        print(count)
        print(dict_elements)
    elif args[1] == '-h' or args[1] == 'help':
        print('''
    getDataip.py <int> // required: <int>
    getDataip.py 0
    getDataip.py 1 <ip> <countdown> // optional: <ip> <countdown>, '-n' for void
    getDataip.py 2 <email> <password> <ip> <hostname> <time_zone> <currency> <security> // required: <email>, <password>, optional: <ip>, <hostname>, <time_zone>, <currency>, <security>
      module    // true or false
    <hostname>  = '-h'  or '-n'
    <time_zone> = '-tz' or   =
    <currency>  = '-c'  or   =
    <security>  = '-s'  or   =
    exemple: 'getDataip.py 2 anything@gmail.com anypassword 0.0.0.0 -h -tz -c -s'
        ''')
except Exception as e:
    print('using command "getDataip.py -h" or "getDataip.py help".')

#getDataip.py <int> // required: <int>
#getDataip.py 0
#getDataip.py 1 <ip> <countdown> // optional: <ip> <countdown>, '-n' for void
#getDataip.py 2 <email> <password> <ip> <hostname> <time_zone> <currency> <security> // required: <email>, <password>, optional: <ip>, <hostname>, <time_zone>, <currency>, <security>
#
#  module    // true or false
#<hostname>  = '-h'  or '-n'
#<time_zone> = '-tz' or   =
#<currency>  = '-c'  or   =
#<security>  = '-s'  or   =

#exemple: 'getDataip.py 2 anything@gmail.com anypassword 0.0.0.0 -h -tz -c -s'