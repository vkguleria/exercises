'''
Input Format

The first line contains 2
space separated integers K and M.
The next K lines each contains an integer Ni , denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

Output Format

Output a single integer denoting the value
Smax
.

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Explanation

Picking 5
from the first list, 9 from the 2nd list and 10 from the 3rd list gives the maximum value equal to  (5**2 + 9**2 + 10**2) % 1000 = 206.

'''
#
'''
lines,modulo=[int(x) for x in input().split()]
max_sq=0
vals=(list(map(int,input().split()[1:])) for _ in range(lines))
max_sq=sum(( max(x)**2 for x in vals ))%modulo
print(max_sq)
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

lines,modulo = (int(x) for x in input().split())
vals = (list(map(int, input().split()))[1:] for _ in range(lines))
results = map(lambda x: sum(i**2 for i in x)%modulo, product(*vals))
#print(*results)
print(max(results))
