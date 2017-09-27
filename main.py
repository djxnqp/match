#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

warningMessage = "usage: python [infile] [step1|step2|cutforstep1]"

if __name__=='__main__':
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "step1"):
            import distinguish_red 
        elif(sys.argv[1] == "step2"):
            import distinguish_group
        elif(sys.argv[1] == "cutforstep1"):
            import cutToRedAndGrooup
        else:
            print warningMessage
    else:
        print warningMessage




