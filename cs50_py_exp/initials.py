#!/usr/bin/python3

initials = input("Print name to get your initials: ").title().split()
print("your initials are: ", end ='')
for i in initials:
    print(i[0],end ='')
print('')    
