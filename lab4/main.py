#!/usr/bin/env python3

import sys

def print_digits(format_string,index):
    buffer=""
    for i in range (index+3,len(format_string)):
        if format_string[i].isdigit():
            buffer += format_string[i]
        elif format_string[i]!=" ":
            return "",index
        else:
            return buffer[::-1],i   
    return "",index

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1]=='g':
                print(param,end="")
                buffer,idx=print_digits(format_string,idx)
                if(buffer!=""):
                    print(" "+buffer,end="")
                shouldDo=False
                
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")




data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
