#!/usr/bin/env python3

import sys

def fexPrint(format_string):
    dict1 = {
        "1":"a",
        "2":"b",
        "3":"c",
        "4":"d",
        "5":"e",
        "6":"f"}
    dict2 = {
        "1":"g",
        "2":"h",
        "3":"i",
        "4":"j",
        "5":"k",
        "6":"l",}
    
    
    
    
    


def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
