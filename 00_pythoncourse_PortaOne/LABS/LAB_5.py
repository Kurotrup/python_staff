#!/usr/bin/python
'''Use the previous task and write a program that checks a connection
 status to a number of remote hosts, but this time create several specialized functions for this.
You should create such functions and use them further in the program:
"read_hosts" - opens a file and reads its content. It should also skip blank lines, alignments, etc.
  expects:
  - a path to a file with addresses
  returns:
  - a list of addresses;
"check" - checks a connection status to a selected host
  expects:
  - address to one host
  - a number of ping tries
  returns:
  - IP address
  - domain name of the host (if exists)
  - % loss
  - max time
"print_res" - prints results to STDOUT and to a file if an optional parameter is given.
 Insert timestamp before printing the results.
  expects:
  - data
  - a file handler or a path to the output file. The output should be printed
   to both STDOUT and the target file if the parameter is set.  '''
import subprocess as sp
import datetime
from sys import argv
from sys import exit
from os import path
def read_hosts(path):
    hosts_l = []
    with open(path) as f:
        for line in f:
            for host in line.split():
                hosts_l.append(host)
    return hosts_l

def check(c,host):
    pg = sp.Popen("ping -c %i -W 2 -q %s" % (c,host),shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    out, err = pg.communicate()
    code = pg.returncode
    if code == 0:
        remote = out.split('\n')[0].split()[2]
        lost = out.split('\n')[3].split(',')[-2].split()[0]
        max = out.split('\n')[4].split(',')[0].split('/')[-2]
    elif code == 1:
        remote,lost,max = None,None,None
    return (host,remote,max,lost)

def print_res(rez_l,out_f=None):
    if out_f is not None:
        print timestamp + '\n'
        f_out.write('\n' + timestamp + '\n\n')
        for host in rez_list:
            print host
            f_out.write(host + '\n')
    else:
        print timestamp + '\n'
        for host in rez_list:
            print host

flag = len(argv)
usage = '\nUsage: ./5.py <inputfile> <count(2 as default)> <outputfile[optional]>\n'
rez_list = []
c = 2
timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")

if flag == 1:
    print 'no arguments' + usage
    exit()
elif flag > 1:
    if path.exists(argv[1]) and path.isfile(argv[1]):
        hosts_list = read_hosts(argv[1])
        if flag > 2:
            if argv[2].isdigit():
                c = int(argv[2])
            else: print usage + 'WARNING:count must be digit, using default value for count\n'
    else: exit('Wrong <inputfile>' + usage)


for host in hosts_list:
    request = check(c,host)
    if request[1] is not None:
        rez_list.append(request[0] + ' ' + request[1] + ': ' + 'max_time = ' + request[2] +' ms; ' + request[3]+' of loss;')
    else:
        rez_list.append(request[0] + ': is unreachable' )

if flag == 4:
    with open(argv[3],'a') as f_out:
        print_res(rez_list,f_out)
else:
    print_res(rez_list)
