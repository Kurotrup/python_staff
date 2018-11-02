#!/usr/bin/python
'''Create a program that checks a date given by a user.
The program accepts dates in two formats:
"May 01 2017" and "12-31-2031".
A name of the month may contain symbols of a mixed case.
The program performs a syntax check and a logical check, i.e.
there is no "Feb 30 2027" or "14-15-2019". As a result,
the program should print on a terminal: "Syntax: OK; Date: valid",
  "Syntax: OK, Date: unreal" or something like that.
Use regular expressions to accomplish the task. '''
from calendar import isleap
import re
import datetime
from sys import exit

def check_date(year,month,day):
    try:
        datetime.datetime(int(year),int(month),int(day))
        return True
    except ValueError:
        return False

matching_dict = {}
months_dict = {'jan':'1','feb':'2','mar':'3','apr':'4','may':'5','jun':'6','jul':'7','aug':'8','sep':'9','oct':'10','nov':'11','dec':'12'}
date_str = raw_input('Program accepts dates in two formats:"May 01 2017" and "12-31-2031"\nEnter your date: ')

match_patern = r'^(?P<month>(?i)[a-z]{3}) (?P<day>\d{1,2}) (?P<year>\d{1,4})$'
matching_dict = re.match(match_patern,date_str.strip()).groupdict()

if matching_dict:
    print ' OK1'
    month = matching_dict['month'].lower()

    if month in months_dict.keys():
        print month
        print months_dict[month]
        matching_dict['month'] = months_dict[month]
        print matching_dict
    else: exit('Wrong syntax')
else:
    match_patern = r'^(?P<month>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{1,4})$'
    matching_dict = re.match(match_patern,date_str.strip()).groupdict()
    if matching_dict:
        print 'OK2'
        print matching_dict

    else: exit('Wrong syntax')
print 'Syntax: OK;',
#print check_date(1988,4,31)
