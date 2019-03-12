#!/usr/bin/env python3


def greatest_common_divisor(a, b):
    while b > 0:
        mod = a % b
        a = b
        b = mod
    return a

def main():
    n = greatest_common_divisor(15, 6)
    print(str(n))
    
 
if __name__ == '__main__':
    main()

