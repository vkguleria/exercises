# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
in_str,size=input().split()
'''
l=[]
for i in range(1,int(size)+1):
    l += [ ''.join(x) for x in combinations(sorted(in_str),i)]
print(*l,sep='\n')
'''
print(*[ ''.join(x) for i in range(1,int(size)+1) for x in combinations(sorted(in_str),i) ], sep="\n")
