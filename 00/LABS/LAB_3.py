#!/usr/bin/python
'''Create a program which returns a service name after giving it a port number.
 A file /etc/services should be used. Usage:
program_name first_port [last_port]
If a second port is mentioned in an argument list, the program should print all
 services that have port numbers in that range.
An output should look like this:
port_number - service.
The program has to process exceptions like blank lines or comments in the file
 and handle an incorrect input from a user.
Notes:
Do not consider tcp/udp differences, return a service name only once
Some ports may be mentioned several times in different parts of the file
Try not to use regular expressions '''
from sys import argv
from sys import exit
flag = len(argv)
portnum1 = 0
ports_and_services = {}
usage = 'Usage: ./13.py <portnumber(start)> <portnumberEnd(optional)>\n'
#input analiz
if flag > 1  and argv[1].isdigit():
    portnum1 = int(argv[1])
    if flag == 3 and argv[2].isdigit():
        if portnum1 < int(argv[2]):
            portnum2 = int(argv[2])
        else:
            print usage + '<portnumberEnd> must be greater then <portnumber(start)>\n'
            exit('Goodbye\n')
elif flag == 1:
    print '\nYou did`t print any port number for service serching'
    print usage
    while flag == 1:
        portnum1 = raw_input('Type port number\n')
        if portnum1.isdigit():
            flag = 0
            portnum1 = int(portnum1)
else:
    print 'Wrong format of variable'
    print usage
    exit('Goodbye\n')
#making dictionary  with port numbers like keys
#fh = open('d:\phyton\WorkHard\Files\services.txt')
fh = open('/etc/services')
for line in fh:
    p=line.split()
    if p and list(p[0])[0] != '#':
        c = int(p[1].split('/')[0])
        if c not in ports_and_services.keys():
            ports_and_services[c] = [p[0]]
        elif p[0] not in ports_and_services[c]:
            ports_and_services[c].append(p[0])
fh.close()
#printing results
if flag == 0 or flag == 2:
    if portnum1 in ports_and_services.keys():
            print str(portnum1) + ' - ' + ', '.join(ports_and_services[portnum1])
    else:
        print 'No such port in usage, try another'
elif flag == 3:
    for i in xrange(portnum1,portnum2):
        if i in ports_and_services.keys():
                print str(i) + ' - ' + ', '.join(ports_and_services[i])
        else:
            print str(i) + ' - ' 'This port is not in usage'
