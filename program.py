#!/usr/bin/python
import math

class utils:
    def reversed(num):
        num = int(num)
        if(num < 0):
            new_num = -1 * (int(str(-1 * num)[::-1]))
        else:
            new_num = int(str(num)[::-1])
        return new_num


    def formatter(num):
        num = int(num)
        oct_num = oct(num)
        bin_num = bin(num)
        return bin_num, oct_num
