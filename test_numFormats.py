'''
Given an integer, n , print the following values for each integer i from 1 to n
:
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each
i from 1 to n . Each value should be space-padded to match the width of the binary value of n.
'''


def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        pass
    l=len(f'{i:0b}')
    for i in range(1,number+1):
        print(f'{i:{l}d} {i:{l}o} {i:{l}X} {i:{l}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
