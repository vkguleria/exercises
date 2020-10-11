# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.groupby returns consecutive keys and groups from the iterable
# input is a string of chars and output is tuple with (no_of_repeatations, item) using groupby
# example output for in_str='1222311':
#    (1, 1) (3, 2) (1, 3) (2, 1)
from itertools import groupby
in_str=input()
print(*[ (len(list(g)),int(k)) for k,g in groupby(in_str) ])
