'''
we need to provide swapcase function that takes a string and returns the string 
with swap_cased characters
sample run:
    # echo "Hi There vINOD ji"|python swap_case.py
alternate sol: return ''.join(map(lambda x: chr(ord(x) ^ 32) if x in string.ascii_letters else x , s))
'''
### sol 1:
#import re
#def swap_case(s):
#    def do_swap(m):
#        return m.group(0).swapcase()
#    return re.sub(r'\w',do_swap,s)
#
### sol 2:
import string
def swap_case(s):
    return ''.join(map(lambda x: chr(ord(x) ^ 32) if x in string.ascii_letters else x , s))
#

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
