#!/usr/bin/python
import os
from sys import argv
from sys import exit
import subprocess as sp

def md5(file_path):
    pg = sp.Popen("md5sum %s" % (file_path),shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    return  pg.communicate()[0].split()[0]

def make_link(orig_path,link_path,c):
    try:
        os.remove(link_path)
        pg = sp.Popen("ln -s %s %s " % (orig_path,link_path),shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
        pg.wait()
        c += 1
    except:
        print 'Can`t remove ' + link_path
    return c

def dublicates_serch(d_name):
    separator = os.sep
    hash_dictionary = {}
    c = 0
    s = 's'
    for (dirname, dirs, files) in os.walk(d_name):
        for file in files:
            file_path = dirname + separator + file
            if not  os.path.islink(file_path):
                if os.path.getsize(file_path) > 0:
                    out = md5(file_path)
                    if out not in hash_dictionary.keys():
                        hash_dictionary[out] = file_path
                    else:
                        c = make_link(hash_dictionary[out],file_path,c)
    if c == 1:
       s = ''
    print 'Created  ' + str(c) +' link' + s

def main():
    flag = len(argv)
    usage = 'USAGE: %s [path] or [nothing for cwd serch ] \n'% os.path.basename(argv[0])
    if flag == 1:
        d_name = '.'
        print 'Scaning curent work directory'
    elif flag > 1 and os.path.exists(argv[1]) and os.path.isdir(argv[1]):
        d_name = argv[1]
    else: exit(usage + 'BAD path to the directory ')

    dublicates_serch(os.path.abspath(d_name))

if __name__ == '__main__':
    main()
