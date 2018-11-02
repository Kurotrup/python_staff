#!/usr/bin/python
import os
from sys import argv
import re

# def build_tree(d,p):
#     for (dirname, dirs, files) in os.walk(d):
#         print p + '+-'+dirname+os.sep
#         #raw_input()
#         p = p + " "
#         for directory in dirs:
#             print p + "|"
#             build_tree(directory,p)
        #print "STTTTTTTTTTOOP"
        #raw_input()

def build_tree(dir, filler):
    print filler[:-1] + '+-' + dir + os.sep
    filler = filler + '--'
    files = os.listdir(dir)
    count = 0

    for file in files:
        count += 1
        print filler + '|'
        path = dir + os.sep + file

        if os.path.isdir(path):
            if count == len(files):
                build_tree(path, filler + ' ')
            else:
                build_tree(path, filler + '|')
        else:
            print filler + '+-' + file

def find_pat(pattern):
    count_match = 0
    pattern = re.compile(pattern)
    for (dirname, dirs, files) in os.walk("."):
        for file in files:
            if pattern.match(file):
                print dirname + os.sep + file
                count_match += 1
    print 'Found ' + str(count_match) + ' matches'

def cwd_size(cwd):
    folder_size = 0
    for (dirname, dirs, files) in os.walk("."):
        for file in files:
            folder_size += os.path.getsize(dirname + os.sep + file)
    return bytes_to_kilo_or_mg(folder_size,cwd)

def bytes_to_kilo_or_mg(folder_size,cwd):
    if folder_size < 1024:
        return 'Size of '+ cwd +'  is ' + folder_size + ' bytes'
    if  1024 <= folder_size < 1024*1024:
        return 'Size of '+ cwd +'  is ' + format((folder_size/1024.),'6.2f') + ' kilobytes'
    if  1024*1024 <= folder_size:
        return 'Size of '+ cwd +'  is ' + format((folder_size/(1024.*1024.)),'8.2f') + ' megabytes'


def main():
    flag = len(argv)
    usage = 'USAGE: %s --find pattern | --tree | --size'% os.path.basename(argv[0])
    cwd = os.getcwd()
    if flag == 1: exit('no arguments\n' + usage)
    elif flag > 1 :
        if argv[1] == '--find':
            if flag > 2:
                pattern = argv[2]
                find_pat(pattern)
            else:exit('no pattern\n' + usage)
        elif argv[1] == '--tree':
            build_tree('.',' ')
        elif argv[1] == '--size':
            print cwd_size(cwd)
        else:exit('unknown argument\n'+ usage)

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == '__main__':
    #main()
    build_tree('.',' ')
    #tree(".",' ')
    #list_files('.')
