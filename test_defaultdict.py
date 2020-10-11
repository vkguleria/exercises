'''
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A . There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Constraints

1<=n<=10000
1<=m<=100
1<=length of each word in input<=100

Input Format

The first line contains integers, n and m separated by a space
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
.

Output Format

Output m
lines.
The ith line should contain the 1-indexed positions of the occurrences of the

ith word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5

'''


from collections import  defaultdict
import sys
n,m = (int(x) for x in input().split())
A= [x for _ in range(n) for x in map(str,input().split()) ]
#print(list(A))
d=defaultdict(list)
for x,i in enumerate(A,1):
    d[i].append(x)
#print(d.items())
B=( x for _ in range(m)  for x in input().split() )
#print(*B)
for i in B:
    if i not in d:
        print(-1,sep=" ")
    else:
        print(*d[i],sep=" ")
