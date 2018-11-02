#!/usr/bin/python
'''Write a program that checks a connection status to a number of remote hosts.
 You should use ping utility for this purpose.
The program reads a list of addresses (domain names and(or) IPs) and for each of
 them tests a connection status.
The usage of the program should be like this:
> ./check_connection.py  input_file  count  [output_file]
where input_file contains target addresses, count - a number of requests for each host, output_file - an optional file to write an output to.
An output should look like:
domain_or_ip_address (remote ip): max_time = X ms; Y% of loss;
If output_file mentioned, the output should be written both to STDOUT and that file,
 if it's not mentioned - then only to STDOUT.
Before writing the results a timestamp should be mentioned. '''
import subprocess as sp
import datetime
from sys import argv
from sys import exit
from os import path
flag = len(argv)
usage = '\nUsage: ./4.py <inputfile> <count(2 as default)> <outputfile[optional]>\n'
hosts_list = []
rez_list = []
c = 2
timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
if flag == 1:
    print 'no arguments' + usage
    exit()
elif flag > 1:
    if path.exists(argv[1]) and path.isfile(argv[1]):
        f = open(argv[1])
        for line in f:
            for host in line.split():
                hosts_list.append(host)
        f.close()
        if flag > 2:
            if argv[2].isdigit():
                c = int(argv[2])
            else: print usage + 'WARNING:count must be digit, using default value for count\n'
    else: exit('Wrong <inputfile>' + usage)
print timestamp + '\n'
for host in hosts_list:
    pg = sp.Popen("ping -c %i -W 2 -q %s" % (c,host),shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    out, err = pg.communicate()
    code = pg.returncode
    if code == 0:
        remote = out.split('\n')[0].split()[2]
        lost = out.split('\n')[3].split(',')[-2].split()[0]
        max = out.split('\n')[4].split(',')[0].split('/')[-2]
        rez_list.append(host + ' ' + remote + ': ' + 'max_time = ' + max +' ms; ' + lost+' of loss;')
    elif code >= 1:
        rez_list.append(host + ': is unreachable' )
    print rez_list[-1]
if flag == 4:
    print "Printing results in  " + argv[3]
    f_out = open(argv[3],'a')
    f_out.write('\n' + timestamp + '\n\n')
    for host in rez_list:
        f_out.write(host + '\n')
    f_out.close()
