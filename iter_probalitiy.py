'''
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N
lowercase English letters. For a given integer K , you can select any K indices (assume 1-

-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K
indices selected will contain the letter: 'a'

Input Format

The input consists of three lines. The first line contains the integer
N , denoting the length of the list. The next line consists of N
space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer

K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the
indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints

All the letters in the list are lowercase English letters.
1 <= N <= 10
1<= K <= N

Sample Input
4
a a c d
2

Sample Output
0.8333

Explanation

All possible unordered tuples of length
comprising of indices from to
are:
(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
Out of these combinations, of them contain either index or index which are the indices that contain the letter 'a'

Hence, the answer is 5/6
'''


from itertools import combinations

items=int(input())
vals=[x for x in input().split()]
num_ind=int(input())
print(*combinations(vals,num_ind))
#combs=[*combinations(list(range(items)),num_ind)]
combs=[*combinations(vals,num_ind)]
#print(combs)
#print(list(filter(lambda x: 'a' in x,combs)))
count= len(list(filter(lambda x: 'a' in x,combs)))
print(f'{round(count/len(combs),4)}')
